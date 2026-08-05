"""
compare.py

Compare LLM generated YAML extractions.

Reads:

results/<spec>/<model>/v4/run1/extracted_parameters.yaml

Generates:

comparisons/comparison_<spec>.md
"""


import yaml
from pathlib import Path


MODELS = [
    "Claude_Sonnet_5",
    "DeepSeek_V4-Flash-0731",
    "Gemini_3",
    "Gemini_3.6_Flash",
    "GLM-5.2",
    "GPT-5.5",
    "Ising-Calibration-1.5",
    "K2.6",
    "Mistral_Medium_3.5",
    "Proprietary_Microsoft_Build",
    "Qwen",
    "Sonar-Perplexity"
]



def load_yaml(path):

    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def extract_parameters(data):

    """
    Convert YAML parameters into dictionary.
    """

    parameters = {}


    # Empty YAML file protection
    if not data:
        return parameters


    yaml_parameters = data.get(
        "parameters",
        []
    )


    # parameters: null protection
    if not yaml_parameters:
        return parameters



    for item in yaml_parameters:

        if not isinstance(item, dict):
            continue


        name = item.get("name")


        if name:

            value = (
                item.get("value")
                or item.get("description")
                or "N/A"
            )


            parameters[name] = value


    return parameters



def find_model_yaml(results_dir, spec, model):

    """
    Search:

    results/
        spec/
            model/
                v4/
                    run1/
                        extracted_parameters.yaml
    """


    yaml_path = (
        Path(results_dir)
        /
        spec
        /
        model
        /
        "v4"
        /
        "run1"
        /
        "extracted_parameters.yaml"
    )


    if yaml_path.exists():

        return yaml_path


    return None



def load_results(results_dir, spec):

    results = {}


    for model in MODELS:

        yaml_file = find_model_yaml(
            results_dir,
            spec,
            model
        )


        if yaml_file:

            print(
                f"Loaded: {model}"
            )

            data = load_yaml(yaml_file)

            results[model] = extract_parameters(data)


        else:

            print(
                f"Skipped: {model} (v4/run1 missing)"
            )

            results[model] = {}


    return results



def generate_table(results):

    """
    Generate markdown comparison table.
    """


    active_models = [
        model
        for model in MODELS
        if results[model]
    ]


    all_parameters = set()


    for model in active_models:

        all_parameters.update(
            results[model].keys()
        )


    all_parameters = sorted(
        all_parameters
    )


    lines = []


    header = [
        "Parameter"
    ] + active_models


    lines.append(
        "| "
        +
        " | ".join(header)
        +
        " |"
    )


    lines.append(
        "| "
        +
        " | ".join(
            ["---"] * len(header)
        )
        +
        " |"
    )


    for parameter in all_parameters:


        row = [
            parameter
        ]


        for model in active_models:

            value = results[model].get(
                parameter,
                "-"
            )


            if isinstance(value, str):

                value = value.replace(
                    "|",
                    "/"
                )


            row.append(
                str(value)
            )


        lines.append(
            "| "
            +
            " | ".join(row)
            +
            " |"
        )


    return "\n".join(lines)



def compare_all():

    results_dir = "results"


    output_dir = Path(
        "comparisons"
    )


    output_dir.mkdir(
        exist_ok=True
    )


    specs = [
        "priveleged_19.3.1",
        "priveleged_2.1"
    ]


    for spec in specs:


        print(
            "\n===================="
        )

        print(
            f"Comparing {spec}"
        )


        results = load_results(
            results_dir,
            spec
        )


        table = generate_table(
            results
        )


        version = spec.replace(
            "priveleged_",
            ""
        )


        output_file = (
            output_dir
            /
            f"comparison_{version}.md"
        )


        output_file.write_text(
            table,
            encoding="utf-8"
        )


        print(
            f"\nSaved: {output_file}"
        )



if __name__ == "__main__":

    compare_all()