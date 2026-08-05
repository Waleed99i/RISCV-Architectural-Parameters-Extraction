'''
Challenge YAML
↓
UnifiedDB YAML
↓
Normalized YAML

Because
    Project Objective 4 literally says export the parameters in UDB yaml format.
    This script directly addresses that objective.
'''

#!/usr/bin/env python3
"""
schema_mapper.py
================

Convert Challenge YAML into UnifiedDB (UDB)-shaped YAML.

Pipeline
--------
Challenge YAML
        ↓
Schema Mapper
        ↓
UnifiedDB-shaped YAML
        ↓
normalized.yaml

Project Objective 4:
Export extracted architectural parameters in UnifiedDB YAML format.

Author:
Muhammad Waleed Akram
"""

from pathlib import Path
import argparse
import yaml


# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_yaml(data, path):
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(
            data,
            f,
            sort_keys=False,
            allow_unicode=True,
            width=120,
        )


# ------------------------------------------------------------
# Normalization
# ------------------------------------------------------------

def normalize_name(name):
    """
    cache block size
        ↓
    CACHE_BLOCK_SIZE
    """

    return (
        name.upper()
        .replace("-", "_")
        .replace(" ", "_")
    )


def normalize_constraints(constraints):

    if constraints is None:
        return {}

    result = {}

    if isinstance(constraints, dict):
        return constraints

    for c in constraints:

        key = (
            c.lower()
            .replace("-", "_")
            .replace(" ", "_")
        )

        result[key] = True

    return result


# ------------------------------------------------------------
# Parameter Mapping
# ------------------------------------------------------------

def map_parameter(param):

    mapped = {
        "name":
            normalize_name(
                param.get("name", "")
            ),

        "description":
            param.get("description", ""),

        "schema": {
            "type":
                param.get("type", "string")
        },

        "constraints":
            normalize_constraints(
                param.get("constraints")
            ),

        "definedBy":
            param.get("defined_by", "implementation"),

        "isaVisible":
            param.get("isa_visible", False),

        "confidence":
            param.get("confidence", "unknown"),

        "evidence": {
            "trigger":
                param.get("trigger"),

            "excerpt":
                param.get("excerpt"),
        }
    }

    return mapped


# ------------------------------------------------------------
# Rejected Candidate Mapping
# ------------------------------------------------------------

def map_rejected(item):

    return {
        "candidate":
            normalize_name(
                item.get("candidate", "")
            ),

        "category":
            item.get("category"),

        "reason":
            item.get("reason"),

        "excerpt":
            item.get("excerpt"),

        "explanation":
            item.get("explanation")
    }


# ------------------------------------------------------------
# Document Mapping
# ------------------------------------------------------------

def map_document(doc):

    output = {
        "schema": "UnifiedDB",

        "version": "0.1",

        "parameters": [],

        "rejected": []
    }

    for p in doc.get("parameters", []):
        output["parameters"].append(
            map_parameter(p)
        )

    for r in doc.get("rejected", []):
        output["rejected"].append(
            map_rejected(r)
        )

    output["parameters"] = sorted(
        output["parameters"],
        key=lambda x: x["name"]
    )

    return output


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------

def main():

    parser = argparse.ArgumentParser(
        description="Challenge YAML → UnifiedDB YAML Mapper"
    )

    parser.add_argument(
        "input",
        help="Challenge YAML"
    )

    parser.add_argument(
        "output",
        help="Output UDB YAML"
    )

    args = parser.parse_args()

    data = load_yaml(args.input)

    mapped = map_document(data)

    save_yaml(mapped, args.output)

    print(f"[✓] Wrote {args.output}")


if __name__ == "__main__":
    main()