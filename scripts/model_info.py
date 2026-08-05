#!/usr/bin/env python3
"""
model_info.py
=============

Generate a markdown table containing metadata for every evaluated model.

Search path:
    results/priveleged_19.3.1/

For every model folder, the script searches recursively for
the first run_metadata.json file.

Output:
    model_comparison/model_info.md
"""

from pathlib import Path
import json

RESULTS_DIR = Path("results/priveleged_19.3.1")
OUTPUT_DIR = Path("model_comparison")
OUTPUT_FILE = OUTPUT_DIR / "model_info.md"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def find_metadata(model_dir):
    """
    Find run_metadata.json anywhere inside a model folder.
    """

    files = sorted(model_dir.rglob("run_metadata.json"))

    if files:
        return files[0]

    return None


def collect_models():

    models = []

    if not RESULTS_DIR.exists():
        raise FileNotFoundError(f"{RESULTS_DIR} not found.")

    for model_dir in sorted(RESULTS_DIR.iterdir()):

        if not model_dir.is_dir():
            continue

        metadata_path = find_metadata(model_dir)

        if metadata_path is None:
            print(f"[WARNING] No metadata found for {model_dir.name}")
            continue

        try:
            data = load_json(metadata_path)

        except Exception as e:
            print(f"[WARNING] Could not read {metadata_path}")
            print(e)
            continue

        models.append({

            "llm_name":
                data.get("llm_name", "-"),

            "provider":
                data.get("provider", "-"),

            "model":
                data.get("model", model_dir.name),

            "context_length":
                data.get("context_length", "-")

        })

    models.sort(key=lambda x: x["model"].lower())

    return models


def generate_markdown(models):

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    lines = []

    lines.append("# Model Information\n")

    lines.append(
        "This table summarizes every Large Language Model used "
        "during benchmarking.\n"
    )

    lines.append(f"**Total Models:** {len(models)}\n")

    lines.append("| LLM | Provider | Model | Context Length |")
    lines.append("|-----|----------|-------|----------------|")

    for m in models:

        lines.append(
            f"| "
            f"{m['llm_name']} | "
            f"{m['provider']} | "
            f"{m['model']} | "
            f"{m['context_length']} |"
        )

    lines.append("\n")

    lines.append("## Notes\n")

    lines.append("- Generated automatically from `run_metadata.json`.")
    lines.append("- One metadata file is read for each model.")
    lines.append("- Metadata is independent of prompt version and benchmark results.")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[✓] Generated {OUTPUT_FILE}")


def main():

    models = collect_models()

    generate_markdown(models)


if __name__ == "__main__":
    main()