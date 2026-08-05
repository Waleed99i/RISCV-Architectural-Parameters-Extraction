# Hallucination Audit - priveleged_2.1


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

snippets/priveleged_2.1.txt


Model outputs:

results/priveleged_2.1/<model>/v4/run1/extracted_parameters.yaml


## Output

Each model folder contains:

hallucination_report.md