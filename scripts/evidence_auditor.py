"""
evidence_auditor.py

Hallucination checker for RISC-V architectural
parameter extraction.

Checks LLM generated YAML evidence against
original RISC-V specification snippets.
"""


import yaml
from pathlib import Path
import difflib


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


SPECS = [
    "priveleged_19.3.1",
    "priveleged_2.1"
]



def load_yaml(path):

    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)



def normalize(text):

    return (
        text
        .lower()
        .replace("\n", " ")
        .strip()
    )



def similarity(a, b):

    return difflib.SequenceMatcher(
        None,
        normalize(a),
        normalize(b)
    ).ratio()



def check_evidence(excerpt, spec_text):

    """
    Check whether extracted evidence
    exists in specification.
    """

    if not excerpt:
        return False, 0.0


    excerpt = normalize(excerpt)

    spec = normalize(spec_text)


    if excerpt in spec:
        return True, 1.0


    score = difflib.SequenceMatcher(
        None,
        excerpt,
        spec
    ).ratio()


    return (
        score >= 0.55,
        score
    )



def extract_parameters(data):

    if not data:
        return []


    parameters = data.get(
        "parameters",
        []
    )


    if not parameters:
        return []


    return parameters



def audit_yaml(yaml_file, spec_text):

    data = load_yaml(
        yaml_file
    )


    results = []


    for param in extract_parameters(data):

        if not isinstance(param, dict):
            continue


        name = param.get(
            "name",
            "UNKNOWN"
        )


        excerpt = param.get(
            "excerpt",
            ""
        )


        found, score = check_evidence(
            excerpt,
            spec_text
        )


        results.append(
            {
                "name": name,
                "excerpt": excerpt,
                "found": found,
                "score": round(score, 2)
            }
        )


    return results



def create_report(
        model,
        spec,
        results,
        output
):


    lines = []


    lines.append(
        "# Hallucination Audit Report\n"
    )


    lines.append(
        f"**Model:** {model}\n"
    )


    lines.append(
        f"**Specification:** {spec}\n"
    )


    lines.append(
        "## Evidence Verification\n"
    )


    lines.append(
        "| Parameter | Evidence Found | Similarity | Status |"
    )

    lines.append(
        "|---|---|---|---|"
    )


    hallucinations = []


    for item in results:


        status = (
            "PASS"
            if item["found"]
            else
            "FAIL"
        )


        if not item["found"]:
            hallucinations.append(
                item["name"]
            )


        lines.append(
            f"| {item['name']} | "
            f"{item['found']} | "
            f"{item['score']} | "
            f"{status} |"
        )


    lines.append(
        "\n## Possible Hallucinations\n"
    )


    if hallucinations:

        for item in hallucinations:

            lines.append(
                f"- {item}"
            )

    else:

        lines.append(
            "No unsupported parameters detected."
        )


    Path(output).write_text(
        "\n".join(lines),
        encoding="utf-8"
    )



def create_readme(spec, folder):

    content = f"""
# Hallucination Audit - {spec}


This folder contains evidence verification reports
for different LLM extraction outputs.


## Methodology

Each extracted YAML file is checked against the
original RISC-V specification text.

The auditor verifies whether:

- extracted parameter evidence exists in the specification
- provided excerpts are supported
- unsupported claims are flagged


## Input

Specification:

snippets/{spec}.txt


Model outputs:

results/{spec}/<model>/v4/run1/extracted_parameters.yaml


## Output

Each model folder contains:

hallucination_report.md
"""


    Path(folder, "README.md").write_text(
        content.strip(),
        encoding="utf-8"
    )



def run_audit():

    for spec in SPECS:


        print(
            f"\nAuditing {spec}"
        )


        snippet_file = (
            Path("snippets")
            /
            f"{spec}.txt"
        )


        if not snippet_file.exists():

            print(
                f"Missing snippet: {snippet_file}"
            )

            continue



        spec_text = snippet_file.read_text(
            encoding="utf-8"
        )


        audit_root = (
            Path("audits")
            /
            spec
        )


        audit_root.mkdir(
            parents=True,
            exist_ok=True
        )


        create_readme(
            spec,
            audit_root
        )



        for model in MODELS:


            yaml_file = (
                Path("results")
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


            if not yaml_file.exists():

                print(
                    f"Skipping {model}"
                )

                continue



            print(
                f"Auditing {model}"
            )


            results = audit_yaml(
                yaml_file,
                spec_text
            )


            model_dir = (
                audit_root
                /
                model
            )


            model_dir.mkdir(
                exist_ok=True
            )


            report = (
                model_dir
                /
                "hallucination_report.md"
            )


            create_report(
                model,
                spec,
                results,
                report
            )



if __name__ == "__main__":

    run_audit()