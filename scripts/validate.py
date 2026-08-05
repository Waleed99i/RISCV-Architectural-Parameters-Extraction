"""
Validate extracted YAML output.

Checks:
- YAML syntax
- Required fields
- Duplicate parameter names
- Confidence value
- Evidence/excerpt presence
- Rejected structure

Automatically validates:
results/
 └── spec/
     └── model/
         └── version/
             └── run/
                 └── extracted_parameters.yaml

Generates:
run/
 └── validation_report.txt
"""

import sys
import yaml
from pathlib import Path


PARAMETER_FIELDS = [
    "name",
    "long_name",
    "description",
    "type",
    "constraints",
    "excerpt",
    "trigger",
    "defined_by",
    "isa_visible",
    "confidence"
]


REJECTED_FIELDS = [
    "candidate",
    "category",
    "reason",
    "excerpt",
    "explanation"
]


VALID_CONFIDENCE = [
    "high",
    "medium",
    "low"
]


def load_yaml(file_path):

    try:

        with open(file_path, "r") as f:
            data = yaml.safe_load(f)

        if data is None:
            return {}

        return data


    except yaml.YAMLError as e:

        print(
            f"YAML parsing error: {e}"
        )

        return None



def validate_parameters(parameters):

    errors = []
    names = set()


    if not isinstance(parameters, list):

        errors.append(
            "'parameters' must be a list"
        )

        return errors



    for idx, param in enumerate(parameters):

        prefix = f"Parameter [{idx}]"


        if not isinstance(param, dict):

            errors.append(
                f"{prefix}: invalid parameter format"
            )

            continue



        # Required fields

        for field in PARAMETER_FIELDS:

            if field not in param:

                errors.append(
                    f"{prefix}: missing field '{field}'"
                )



        # Duplicate names

        if "name" in param:

            if param["name"] in names:

                errors.append(
                    f"{prefix}: duplicate parameter name '{param['name']}'"
                )


            names.add(
                param["name"]
            )



        # Confidence validation

        if "confidence" in param:

            if param["confidence"] not in VALID_CONFIDENCE:

                errors.append(
                    f"{prefix}: invalid confidence '{param['confidence']}'"
                )



        # Evidence check

        if not param.get("excerpt"):

            errors.append(
                f"{prefix}: missing evidence excerpt"
            )



        # isa_visible type check

        if "isa_visible" in param:

            if not isinstance(param["isa_visible"], bool):

                errors.append(
                    f"{prefix}: isa_visible must be boolean"
                )


    return errors




def validate_rejected(rejected):

    errors = []


    if not isinstance(rejected, list):

        errors.append(
            "'rejected' must be a list"
        )

        return errors



    for idx, item in enumerate(rejected):

        for field in REJECTED_FIELDS:

            if field not in item:

                errors.append(
                    f"Rejected [{idx}]: missing '{field}'"
                )


    return errors




def validate_file(file_path):

    data = load_yaml(file_path)


    if data is None:

        return False, [
            "YAML parsing failed"
        ]



    errors = []



    if "parameters" not in data:

        errors.append(
            "Missing top-level 'parameters'"
        )


    else:

        errors.extend(
            validate_parameters(
                data["parameters"]
            )
        )



    if "rejected" in data:

        errors.extend(
            validate_rejected(
                data["rejected"]
            )
        )



    if errors:

        return False, errors



    return True, []




def save_report(run_dir, model, version, run, passed, errors):

    report_file = (
        run_dir /
        "validation_report.txt"
    )


    with open(report_file, "w") as f:


        f.write(
            "RISC-V Architectural Parameter Extraction Validation\n"
        )

        f.write(
            "=" * 60 +
            "\n\n"
        )


        f.write(
            f"LLM Model : {model}\n"
        )

        f.write(
            f"Version   : {version}\n"
        )

        f.write(
            f"Run       : {run}\n\n"
        )



        if passed:

            f.write(
                "Status : PASSED\n\n"
            )

            f.write(
                "Errors : None\n"
            )


        else:

            f.write(
                "Status : FAILED\n\n"
            )


            f.write(
                "Errors:\n"
            )


            for error in errors:

                f.write(
                    f"- {error}\n"
                )




def main():

    if len(sys.argv) != 2:

        print(
            "Usage: python validate.py <results_directory>"
        )

        sys.exit(1)



    results_path = Path(
        sys.argv[1]
    )



    if not results_path.exists():

        print(
            "Directory does not exist"
        )

        sys.exit(1)



    total = 0
    passed = 0
    failed = 0



    print("\n")
    print("=" * 60)
    print(
        "RISC-V Architectural Parameter Extraction Validation"
    )
    print("=" * 60)



    # MODEL LOOP

    for model_dir in sorted(results_path.iterdir()):


        if not model_dir.is_dir():
            continue



        model_name = model_dir.name



        print("\n")
        print("=" * 50)
        print(
            f"LLM Model: {model_name}"
        )
        print("=" * 50)



        # VERSION LOOP

        for version_dir in sorted(model_dir.iterdir()):


            if not version_dir.is_dir():
                continue



            print(
                f"\nVersion: {version_dir.name}"
            )



            # RUN LOOP

            for run_dir in sorted(version_dir.iterdir()):


                if not run_dir.is_dir():
                    continue



                print(
                    f"\n  {run_dir.name}"
                )



                yaml_file = (
                    run_dir /
                    "extracted_parameters.yaml"
                )



                if not yaml_file.exists():

                    print(
                        "  ⚠️ Missing extracted_parameters.yaml"
                    )

                    continue



                total += 1



                status, errors = validate_file(
                    yaml_file
                )



                save_report(
                    run_dir,
                    model_name,
                    version_dir.name,
                    run_dir.name,
                    status,
                    errors
                )



                if status:

                    print(
                        "  ✅ PASSED"
                    )

                    passed += 1



                else:

                    print(
                        "  ❌ FAILED"
                    )


                    for error in errors:

                        print(
                            f"     - {error}"
                        )


                    failed += 1



    print("\n")
    print("=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)


    print(
        f"Total Runs   : {total}"
    )

    print(
        f"Passed       : {passed}"
    )

    print(
        f"Failed       : {failed}"
    )



    if total > 0:

        accuracy = (
            passed / total
        ) * 100


        print(
            f"Success Rate : {accuracy:.2f}%"
        )



if __name__ == "__main__":
    main()