<div align="center">


# AI-Assisted Extraction of RISC-V Architectural Parameters using Large Language Models



</div>


![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![RISC-V](https://img.shields.io/badge/RISC--V-ISA-red?style=for-the-badge)
![LLM](https://img.shields.io/badge/12-LLMs-blueviolet?style=for-the-badge)
![Prompt](https://img.shields.io/badge/Prompt-V1→V4-success?style=for-the-badge)
![Validation](https://img.shields.io/badge/YAML-Validation-green?style=for-the-badge)
![Evidence](https://img.shields.io/badge/Evidence-Auditing-orange?style=for-the-badge)
![Ground Truth](https://img.shields.io/badge/Ground-Truth-yellow?style=for-the-badge)
![UDB](https://img.shields.io/badge/UDB-Compatible-red?style=for-the-badge)

*Benchmarking • Prompt Engineering • Validation • Evidence Auditing • UnifiedDB YAML Generation*

## Project Overview

This project investigates the use of Large Language Models (LLMs) for the automated extraction of architectural parameters from the RISC-V ISA specifications and their transformation into structured, machine-readable representations suitable for the RISC-V Unified Database (UDB). The work focuses on the complete extraction workflow rather than simply asking an LLM to identify parameters: specification snippets are processed through progressively refined prompts, candidate parameters are identified and classified, extracted information is validated, supporting evidence is audited, and outputs from multiple models and repeated runs are compared against a manually prepared ground-truth baseline. The project benchmarks 12 different LLMs and evaluates their ability to distinguish genuine architectural parameters from constants, constraints, implementation-specific details, and unsupported candidates. The final stage maps the validated extraction results into UDB-shaped YAML, providing an end-to-end and reproducible workflow that connects natural-language RISC-V specifications with structured architectural data.

## Snippets
- [Priveleged 19.3.1](snippets/priveleged_19.3.1.txt)
- [Priveleged 2.1](snippets/priveleged_2.1.txt)

# Approach

```mermaid
flowchart LR
    A["RISC-V Specification"] --> V1["V1<br/>Baseline Extraction"]
    V1 --> V2["V2<br/>Candidate Rejection"]
    V2 --> V3["V3<br/>Evidence-Driven"]
    V3 --> V4["V4<br/>Full Validation Pipeline"]

    V1 -.-> B1["Extract"]
    V2 -.-> B2["Classify + Reject"]
    V3 -.-> B3["Verify Evidence"]
    V4 -.-> B4["Validate + Generate"]

    V4 --> OUT["Structured<br/>YAML Output"]

    style A stroke-width:2px
    style V1 stroke-width:2px
    style V2 stroke-width:2px
    style V3 stroke-width:2px
    style V4 stroke-width:3px
    style OUT stroke-width:2px
```

The prompt architecture was developed iteratively from a basic extraction prompt into a structured, evidence-aware and validation-oriented workflow. Each version addresses limitations identified in the previous version while keeping the output schema sufficiently consistent for comparison.

## Prompt Evolution

| Version                                                                                                                            | Focus             | Main Improvement                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **[V1 — Baseline Extraction](https://github.com/Waleed99i/RISCV-Architectural-Parameters-Extraction/tree/main/prompts/v1)**        | Direct extraction | Establishes the basic parameter extraction and YAML generation workflow.                                                    |
| **[V2 — Candidate Rejection](https://github.com/Waleed99i/RISCV-Architectural-Parameters-Extraction/tree/main/prompts/v2)**        | Classification    | Adds explicit rejection of non-architectural candidates and architectural validation.                                       |
| **[V3 — Evidence-Driven Extraction](https://github.com/Waleed99i/RISCV-Architectural-Parameters-Extraction/tree/main/prompts/v3)** | Evidence          | Adds evidence excerpts, trigger tracking, confidence, and stronger constraint verification.                                 |
| **[V4 — Production Pipeline](https://github.com/Waleed99i/RISCV-Architectural-Parameters-Extraction/tree/main/prompts/v4)**        | Full workflow     | Combines detection, rejection, validation, evidence verification, constraint checking and automation-ready YAML generation. |

Each prompt version contains the same four supporting files:

* `system_prompt.md` — defines the model's role, rules and extraction methodology.
* `user_prompt.md` — provides the specification input and task instructions.
* `expected_output_schema.yaml` — defines the required YAML output structure.
* `README.md` — documents the purpose and behavior of that prompt version.

---

# Best Version: V4

**V4 is the final and most complete prompt architecture developed in the project.** Rather than treating extraction as a single LLM operation, it organizes the task into a sequence of checks covering candidate identification, rejection, architectural relevance, evidence, constraints and structured output. This makes V4 suitable not only for individual extraction experiments but also for the automated benchmarking and validation pipeline used throughout the repository.

| Capability                   |  V1 |    V2   |    V3   |  V4 |
| ---------------------------- | :-: | :-----: | :-----: | :-: |
| Parameter extraction         |  ✓  |    ✓    |    ✓    |  ✓  |
| YAML formatting              |  ✓  |    ✓    |    ✓    |  ✓  |
| Candidate rejection          |  ✗  |    ✓    |    ✓    |  ✓  |
| Architectural validation     |  ✗  |    ✓    |    ✓    |  ✓  |
| ISA visibility analysis      |  ✗  |    ✓    |    ✓    |  ✓  |
| Evidence excerpts            |  ✗  |    ✗    |    ✓    |  ✓  |
| Trigger tracking             |  ✗  |    ✗    |    ✓    |  ✓  |
| Confidence estimation        |  ✗  |    ✗    |    ✓    |  ✓  |
| Constraint verification      |  ✗  | Partial |    ✓    |  ✓  |
| Rejection explanations       |  ✗  |    ✓    |    ✓    |  ✓  |
| Automation-ready output      |  ✗  | Partial | Partial |  ✓  |
| Production benchmark support |  ✗  |    ✗    | Partial |  ✓  |

### V4 Workflow


```mermaid
flowchart TD
    A["V4 Input<br/>RISC-V Specification Snippet"]

    A --> T1["T1 — Candidate Detection<br/>Identify parameter-like statements"]
    T1 --> T2["T2 — Candidate Classification<br/>Parameter or non-parameter?"]
    T2 --> T3["T3 — Evidence Verification<br/>Verify supporting specification text"]
    T3 --> T4["T4 — Architectural Validation<br/>Confirm architectural significance"]
    T4 --> T5["T5 — Constraint Extraction<br/>Determine type and constraints"]
    T5 --> T6["T6 — YAML Generation<br/>Produce structured parameter output"]

    T6 --> O["Extracted Architectural Parameters"]

    T2 -. "Rejected candidate" .-> R["Candidate Rejected"]
    T3 -. "Unsupported evidence" .-> R
    T4 -. "Not architectural" .-> R
```

# Models Evaluated

The project evaluates **12 Large Language Models from 12 different model/provider ecosystems**, allowing the extraction pipeline to be tested across models with substantially different architectures, context limits, and capabilities. All models were evaluated using the same specification snippets and the same prompt-generation methodology, with the purpose of comparing extraction quality, consistency, evidence handling, and architectural classification rather than relying on the behavior of a single model. The evaluated models are **Claude Sonnet 5 (Anthropic)**, **DeepSeek V4-Flash-0731 (DeepSeek)**, **Gemini 3 (Google)**, **Gemini 3.6 Flash (Google)**, **GLM-5.2 (Zhipu AI)**, **GPT-5.5 (OpenAI)**, **Ising-Calibration-1.5 (NVIDIA)**, **K2.6 (Moonshot AI)**, **Mistral Medium 3.5 (Mistral AI)**, **Proprietary Microsoft Build (Microsoft/Copilot)**, **Qwen (Alibaba Tongyi Lab)**, and **Sonar-Perplexity (Perplexity AI)**. Their reported context capacities range from **4,096 tokens to more than one million tokens**, making the benchmark representative of models with significantly different context capabilities. The model information is maintained separately in the repository so that each experiment can be associated with the exact model configuration used during extraction.

| Model                       | Provider           |             Reported Context Length |
| --------------------------- | ------------------ | ----------------------------------: |
| Claude Sonnet 5             | Anthropic          |                    1,048,576 tokens |
| DeepSeek V4-Flash-0731      | DeepSeek           |                    1,048,576 tokens |
| Gemini 3                    | Google             |                     Up to 1M tokens |
| Gemini 3.6 Flash            | Google             |                    1,048,576 tokens |
| GLM-5.2                     | Zhipu AI           |                         128K tokens |
| GPT-5.5                     | OpenAI             |                    1,048,576 tokens |
| Ising-Calibration-1.5       | NVIDIA             |                        4,096 tokens |
| K2.6                        | Moonshot AI        | 256K tokens; 2M characters extended |
| Mistral Medium 3.5          | Mistral AI         |                          32K tokens |
| Proprietary Microsoft Build | Microsoft          |              Not publicly disclosed |
| Qwen                        | Alibaba Tongyi Lab |                  Up to 256K+ tokens |
| Sonar-Perplexity            | Perplexity AI      |                         128K tokens |

## Python Scripts

The repository contains a set of Python scripts that automate the extraction, validation, analysis, auditing, comparison, and UDB-mapping stages of the project. Each script has a specific role in the overall pipeline, allowing the experimental workflow to remain modular and reproducible.

| **Script**                                                                                                                                              | **Description**                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**extract.py**](https://github.com/Waleed99i/RISCV-Architectural-Parameters-Extraction/blob/main/scripts/extract.py)                                   | Executes the extraction workflow by sending prompts to different LLMs, storing raw responses, generating extracted YAML files, and maintaining run metadata.                                                                              |
| [**validate.py**](https://github.com/Waleed99i/RISCV-Architectural-Parameters-Extraction/blob/main/scripts/validate.py)                                 | Performs automated YAML validation by checking required fields, schema compliance, and output formatting. It generates `validation_report.md` inside each model run.                                                                      |
| [**candidate_detector.py**](https://github.com/Waleed99i/RISCV-Architectural-Parameters-Extraction/blob/main/scripts/candidate_detector.py)             | Performs general candidate extraction from specification snippets to identify possible architectural parameters.                                                                                                                          |
| [**riscv_candidate_detector.py**](https://github.com/Waleed99i/RISCV-Architectural-Parameters-Extraction/blob/main/scripts/riscv_candidate_detector.py) | Applies RISC-V-specific filtering and categorization to identify architecture-relevant candidates from the detected set.                                                                                                                  |
| [**compare.py**](https://github.com/Waleed99i/RISCV-Architectural-Parameters-Extraction/blob/main/scripts/compare.py)                                   | Compares outputs across different LLMs and generates comparative reports for the evaluated specification sections.                                                                                                                        |
| [**evidence_auditor.py**](https://github.com/Waleed99i/RISCV-Architectural-Parameters-Extraction/blob/main/scripts/evidence_auditor.py)                 | Performs evidence and hallucination auditing by checking whether extracted evidence exists, matches the provided specification, and whether unsupported parameters were introduced.                                                       |
| [**model_info.py**](https://github.com/Waleed99i/RISCV-Architectural-Parameters-Extraction/blob/main/scripts/model_info.py)                             | Collects metadata for the tested models, including provider, model name, and reported context length.                                                                                                                                     |
| [**schema_mapper.py**](https://github.com/Waleed99i/RISCV-Architectural-Parameters-Extraction/blob/main/scripts/schema_mapper.py)                       | Converts challenge-style YAML into normalized YAML and ultimately maps the extracted parameters into [**RISC-V Unified Database (UDB) YAML**](https://github.com/Waleed99i/RISCV-Architectural-Parameters-Extraction/tree/main/UDB_YAML). |
| [**report_generator.py**](https://github.com/Waleed99i/RISCV-Architectural-Parameters-Extraction/blob/main/scripts/report_generator.py)                 | Automates generation of final reports and summaries from the experimental outputs.                                                                                                                                                        |

## Model Comparison

The [`compare.py`](https://github.com/Waleed99i/RISCV-Architectural-Parameters-Extraction/blob/main/scripts/compare.py) script compares the parameters extracted by different LLMs for the same specification snippet. It places model outputs side by side to identify common parameters, differences in extraction, and variations in parameter naming or descriptions.

### Privileged ISA §19.3.1 — Cache Blocks

| Parameter              | DeepSeek_V4-Flash-0731                                                                                                                                                                  | Gemini_3                                                                                                        | Gemini_3.6_Flash                                                                                             | GLM-5.2                                                                                     | GPT-5.5                                                                         | Ising-Calibration-1.5                           | K2.6                         | Proprietary_Microsoft_Build                                                                     | Qwen                                           | Sonar-Perplexity                                                                     |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------ |
| **CACHE_BLOCK_SIZE**   | The size of a cache block, representing a contiguous, naturally aligned power-of-two (or NAPOT) range of memory locations. Uniform throughout the system in the initial CMO extensions. | The size of a cache block, representing a contiguous, naturally aligned power-of-two range of memory locations. | -                                                                                                            | -                                                                                           | Implementation-specific size of a cache block that is discoverable by software. | -                                               | -                            | The size of a cache block is implementation-specific but must be uniform throughout the system. | Implementation-specific size of a cache block. | -                                                                                    |
| **CACHE_CAPACITY**     | The total data storage capacity of a cache.                                                                                                                                             | The total storage capacity of the cache.                                                                        | -                                                                                                            | -                                                                                           | -                                                                               | -                                               | -                            | The total capacity of a cache is implementation-specific.                                       | -                                              | -                                                                                    |
| **CACHE_ORGANIZATION** | The structural arrangement of a cache.                                                                                                                                                  | The structural organization of the cache.                                                                       | -                                                                                                            | -                                                                                           | -                                                                               | -                                               | -                            | The organization of a cache is implementation-specific.                                         | -                                              | -                                                                                    |
| **CacheBlockSize**     | -                                                                                                                                                                                       | -                                                                                                               | -                                                                                                            | -                                                                                           | -                                                                               | The size of a cache block in bytes.             | -                            | -                                                                                               | -                                              | -                                                                                    |
| **CacheCapacity**      | -                                                                                                                                                                                       | -                                                                                                               | -                                                                                                            | -                                                                                           | -                                                                               | The total storage capacity of a cache in bytes. | -                            | -                                                                                               | -                                              | -                                                                                    |
| **cache_block_size**   | -                                                                                                                                                                                       | -                                                                                                               | The size of a cache block in bytes, representing a contiguous, naturally aligned power-of-two (NAPOT) range. | The size of a cache block, which is implementation-specific and discoverable by software.   | -                                                                               | -                                               | The size of a cache block.   | -                                                                                               | -                                              | The size of a cache block is implementation-specific and discoverable by software.   |
| **cache_capacity**     | -                                                                                                                                                                                       | -                                                                                                               | -                                                                                                            | The capacity of a cache, which is implementation-specific and discoverable by software.     | -                                                                               | -                                               | The capacity of a cache.     | -                                                                                               | -                                              | The capacity of a cache is implementation-specific and discoverable by software.     |
| **cache_organization** | -                                                                                                                                                                                       | -                                                                                                               | -                                                                                                            | The organization of a cache, which is implementation-specific and discoverable by software. | -                                                                               | -                                               | The organization of a cache. | -                                                                                               | -                                              | The organization of a cache is implementation-specific and discoverable by software. |

### Privileged ISA §2.1 — CSR Address Space

The same comparison was performed for **Privileged ISA §2.1**, with the generated outputs compared across all evaluated models.
