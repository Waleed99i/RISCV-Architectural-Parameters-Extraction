#!/usr/bin/env python3

"""
AI-assisted Architectural Parameter Extraction Pipeline

Author : Muhammad Waleed Akram
Project: LFX 2026 Parameter Extraction Coding Challenge

Responsibilities
----------------
1. Select prompt version.
2. Select snippet.
3. Select model/provider.
4. Accept raw LLM response.
5. Extract YAML from response.
6. Validate YAML.
7. Generate repository structure.
8. Save:
      raw_response.md
      extracted_parameters.yaml
      run_metadata.json
"""

from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import yaml
import textwrap
import os
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent

PROMPTS_DIR = ROOT_DIR / "prompts"
SNIPPETS_DIR = ROOT_DIR / "snippets"
RESULTS_DIR = ROOT_DIR / "results"

SUPPORTED_MODELS = {

    "1": {
        "llm_name": "ChatGPT",
        "provider": "OpenAI",
        "model": "GPT-5.5",
        "context_length": "1,048,576 tokens"
    },

    "2": {
        "llm_name": "Gemini",
        "provider": "Google",
        "model": "Gemini 3.6 Flash",
        "context_length": "1,048,576 tokens"
    },

    "3": {
        "llm_name": "DeepSeek",
        "provider": "DeepSeek",
        "model": "DeepSeek V4-Flash-0731",
        "context_length": "1,048,576 tokens"
    },

    "4": {
        "llm_name": "Claude",
        "provider": "Anthropic",
        "model": "Claude Sonnet 5",
        "context_length": "1,048,576 tokens"
    },

    "5": {
        "llm_name": "Kimi",
        "provider": "Moonshot AI",
        "model": "K2.6",
        "context_length": "256K tokens (2M characters extended)"
    },

    "6": {
        "llm_name": "Copilot",
        "provider": "Microsoft",
        "model": "Proprietary Microsoft Build",
        "context_length": "Not publicly disclosed"
    },

    "7": {
        "llm_name": "Gemini",
        "provider": "Google",
        "model": "Gemini 3",
        "context_length": "Up to 1M tokens"
    },

    "8": {
        "llm_name": "NVIDIA",
        "provider": "NVIDIA",
        "model": "Ising-Calibration-1.5",
        "context_length": "4096 tokens"
    },

    "9": {
        "llm_name": "Qwen",
        "provider": "Alibaba Tongyi Lab",
        "model": "Qwen",
        "context_length": "Up to 256K+ tokens"
    },

    "10": {
        "llm_name": "Custom",
        "provider": "",
        "model": "",
        "context_length": ""
    }

}

def banner():

    print("=" * 70)
    print("AI-assisted Architectural Parameter Extraction")
    print("=" * 70)
    print()

def discover_prompt_versions():

    versions = []

    for directory in sorted(PROMPTS_DIR.iterdir()):

        if directory.is_dir():

            if (directory / "system_prompt.md").exists():

                versions.append(directory.name)

    return versions

def discover_snippets():

    snippets = []

    for file in sorted(SNIPPETS_DIR.glob("*.txt")):

        snippets.append(file)

    return snippets

def choose(title, options):

    print()

    print(title)

    print("-" * len(title))

    for i, option in enumerate(options, start=1):

        print(f"{i}. {option}")

    print()

    while True:

        choice = input("Selection: ").strip()

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(options):

                return options[choice - 1]

        print("Invalid selection.\n")

def choose_model():

    print()
    print("Available Models")
    print("----------------")

    for key, value in SUPPORTED_MODELS.items():

        if value["llm_name"] == "Custom":
            print(f"{key}. Custom")
        else:
            print(f'{key}. {value["llm_name"]} ({value["model"]})')

    while True:

        selection = input("\nSelection: ").strip()

        if selection not in SUPPORTED_MODELS:
            continue

        model = SUPPORTED_MODELS[selection]

        if model["llm_name"] == "Custom":

            return {
                "llm_name": input("LLM Name        : "),
                "provider": input("Provider        : "),
                "model": input("Version         : "),
                "context_length": input("Context Length  : ")
            }

        return model
    
def read_response():

    print()

    print("Paste complete LLM response.")

    print("Finish with Ctrl+D (Linux/macOS)")

    print("or Ctrl+Z then Enter (Windows).\n")

    try:

        text = sys.stdin.read()

    except KeyboardInterrupt:

        sys.exit()

    return text.strip()

def extract_yaml(raw):

    pattern = r"```yaml(.*?)```"

    match = re.search(pattern, raw, flags=re.DOTALL | re.IGNORECASE)

    if match:

        return textwrap.dedent(match.group(1)).strip()

    return raw.strip()

def validate_yaml(text):

    try:

        data = yaml.safe_load(text)

    except yaml.YAMLError as e:

        print()

        print("Invalid YAML")

        print(e)

        sys.exit()

    if not isinstance(data, dict):

        print("Top level must be dictionary.")

        sys.exit()

    return data

def sha16(path):

    text = path.read_text()

    return hashlib.sha256(text.encode()).hexdigest()[:16]

def timestamp():

    return datetime.now(timezone.utc).isoformat()

# ============================================================
# Create Results Directory
# ============================================================

def create_results_directory(snippet_name,
                             model_name,
                             prompt_version,
                             run_number):

    path = (
        RESULTS_DIR
        / snippet_name
        / model_name.replace(" ", "_")
        / prompt_version
        / f"run{run_number}"
    )

    path.mkdir(parents=True, exist_ok=True)

    return path

# ============================================================
# Save Raw Response
# ============================================================

def save_raw_response(directory, raw_response):

    file = directory / "raw_response.md"

    file.write_text(raw_response, encoding="utf-8")

# ============================================================
# Save Clean YAML
# ============================================================

def save_yaml(directory, yaml_text):

    file = directory / "extracted_parameters.yaml"

    file.write_text(yaml_text, encoding="utf-8")

# ============================================================
# Generate Metadata
# ============================================================

def generate_metadata(model_info,
                      prompt_version,
                      snippet,
                      run_number,
                      raw_response):

    system_prompt = (
        PROMPTS_DIR
        / prompt_version
        / "system_prompt.md"
    )

    user_prompt = (
        PROMPTS_DIR
        / prompt_version
        / "user_prompt.md"
    )

    metadata = {

        "schema": "parameter_extraction_run/1.0",

        "timestamp_utc": timestamp(),

        "llm_name": model_info["llm_name"],
        "provider": model_info["provider"],
        "model": model_info["model"],
        "context_length": model_info["context_length"],

        "prompt_version": prompt_version,

        "snippet": snippet,

        "run": run_number,

        "response_source": "manual_copy",

        "status": "success",

        "prompt_sha256_16": {

            "system": sha16(system_prompt),

            "user": sha16(user_prompt)

        },

        "raw_response_characters": len(raw_response),

        "yaml_generated": True

    }

    return metadata

# ============================================================
# Save Metadata
# ============================================================

def save_metadata(directory, metadata):

    file = directory / "run_metadata.json"

    with open(file, "w", encoding="utf-8") as f:

        json.dump(metadata, f, indent=4)

    
# ============================================================
# Summary
# ============================================================

def print_summary(directory):

    print()

    print("=" * 70)

    print("Extraction Completed Successfully")

    print("=" * 70)

    print()

    print("Generated Files")

    print("----------------")

    print(directory / "raw_response.md")

    print(directory / "extracted_parameters.yaml")

    print(directory / "run_metadata.json")

    print()

# ============================================================
# Main
# ============================================================

def main():

    banner()

    prompt_versions = discover_prompt_versions()

    snippets = discover_snippets()

    prompt_version = choose(

        "Available Prompt Versions",

        prompt_versions

    )

    snippet_path = choose(

        "Available Snippets",

        snippets

    )

    model_info = choose_model()

    print()

    run_number = input("Run Number : ").strip()

    if run_number == "":

        run_number = "1"

    raw_response = read_response()

    yaml_text = extract_yaml(raw_response)

    validate_yaml(yaml_text)

    snippet_name = snippet_path.stem

    results_directory = create_results_directory(
        snippet_name,
        model_info["model"],
        prompt_version,
        run_number
    )

    save_raw_response(

        results_directory,

        raw_response

    )

    save_yaml(

        results_directory,

        yaml_text

    )

    metadata = generate_metadata(
        model_info,
        prompt_version,
        snippet_name,
        run_number,
        raw_response
    )

    save_metadata(

        results_directory,

        metadata

    )

    print_summary(

        results_directory

    )


if __name__ == "__main__":

    main()

