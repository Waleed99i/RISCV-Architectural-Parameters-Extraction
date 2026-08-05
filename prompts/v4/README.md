# Prompt Version 4

Production-grade architectural parameter extraction pipeline for the RISC-V ISA.

Unlike previous prompt versions, V4 introduces a structured multi-stage extraction workflow that separates candidate discovery, architectural validation, evidence verification, and final YAML generation. The goal is to maximize precision while minimizing hallucinations and unsupported architectural inferences.

---

# Evolution

```mermaid
flowchart LR

V1["V1<br/>Baseline Extraction"]
--> V2["V2<br/>Decision-Based Verification"]
--> V3["V3<br/>Evidence-Driven Extraction"]
--> V4["V4<br/>Production Pipeline"]
```

---

# Overall Pipeline

```mermaid
flowchart LR

A["Specification"]
--> B["T1<br/>Candidate Detection"]
--> C["T2<br/>Classification"]
--> D["T3<br/>Evidence Verification"]
--> E["T4<br/>Architectural Validation"]
--> F["T5<br/>Constraint Extraction"]
--> G["T6<br/>YAML Generation"]
```

---

# Acceptance Workflow

```mermaid
flowchart TD

A["Candidate"]

A --> B{"Implementation Choice?"}

B -- No --> X["Reject"]

B -- Yes --> C{"ISA Visible?"}

C -- No --> X

C -- Yes --> D{"Explicit Evidence?"}

D -- No --> X

D -- Yes --> E["Accepted Parameter"]

E --> F["Generate YAML"]
```

---

# Extraction Pipeline

## T1 — Candidate Detection

Identify every phrase that could reasonably represent an architectural parameter.

No validation is performed during this stage.

Goal:

- High recall
- Maximum candidate coverage

---

## T2 — Parameter Classification

Classify every candidate into one of the following categories.

- Architectural Parameter
- Architectural Constraint
- Architectural Constant
- Descriptive Information
- Microarchitectural Detail
- Other

Only Architectural Parameters continue.

---

## T3 — Evidence Verification

Every accepted parameter must be supported by an exact verbatim excerpt copied from the specification.

If exact evidence cannot be produced, the candidate is rejected.

---

## T4 — Architectural Validation

Verify that the candidate satisfies all architectural requirements.

A valid parameter must

- represent an implementation choice
- be observable through the ISA
- be explicitly supported by the supplied text
- not simply describe architectural facts

---

## T5 — Constraint Extraction

Extract only constraints explicitly stated by the specification.

Examples include

- implementation-specific
- implementation-defined
- discoverable
- power-of-two
- alignment requirements
- minimum values
- maximum values

No inferred constraints are permitted.

---

## T6 — YAML Generation

Produce deterministic YAML matching the expected schema.

Only accepted parameters appear in the final output.

Rejected candidates are reported separately.

---

# Decision Process

```mermaid
graph TD

Specification

Specification --> Candidate

Candidate --> Evidence

Evidence --> Validation

Validation --> Accepted

Validation --> Rejected

Accepted --> YAML

Rejected --> Report
```

---

# Improvements over V3

| Capability | V3 | V4 |
|------------|----|----|
| Candidate Detection | ✓ | ✓ |
| Evidence Verification | ✓ | ✓ |
| Architectural Validation | ✓ | ✓ |
| Constraint Extraction | ✓ | ✓ |
| Rich Rejection Categories | Limited | ✓ |
| Deterministic Output | Partial | ✓ |
| Automation Compatible | Partial | ✓ |
| UDB-aware Workflow | Limited | ✓ |

---



# Generated Outputs

```text
raw_response.md
extracted_parameters.yaml
run_metadata.json
```

---

# Objective

The purpose of V4 is to produce reproducible, specification-grounded architectural parameter extraction with deterministic outputs suitable for automated validation, benchmarking, and comparison across multiple Large Language Models.