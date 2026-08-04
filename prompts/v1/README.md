# Prompt Version 1 — Baseline Architectural Parameter Extraction

## Overview

Version 1 establishes the baseline prompt used for architectural parameter extraction from RISC-V ISA specification snippets.

The objective is to identify implementation-dependent architectural parameters while producing structured YAML output.

No multi-stage reasoning or validation pipeline is used in this version.

---

## Design Goals

- Build a simple baseline extraction prompt.
- Produce deterministic YAML output.
- Avoid unnecessary prompt complexity.
- Minimize hallucinations through basic extraction rules.
- Establish a reference point for later prompt iterations.

---

## Prompt Components

### System Prompt

Defines:

- architectural parameter
- extraction rules
- naming conventions
- supported parameter types
- output formatting

### User Prompt

Supplies the ISA snippet for extraction.

### Output Schema

Defines the expected YAML structure.

---

## Output Format

Each extracted parameter contains:

- name
- description
- type
- constraints

---

## Current Limitations

Version 1 intentionally keeps reasoning simple.

It does **not**:

- distinguish architectural parameters from microarchitectural choices
- verify ISA visibility
- classify rejected candidates
- verify textual evidence
- validate generated constraints
- perform confidence estimation

These capabilities are introduced in later prompt versions.

---

## Expected Behaviour

Version 1 generally performs well on straightforward implementation-defined parameters but may produce:

- false positives
- unsupported constraints
- inconsistent naming
- missing justification

These shortcomings motivate the improvements introduced in Versions 2–4.