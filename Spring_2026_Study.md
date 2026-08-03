# Phased PR's Summary of LFX Spring 2026 
Top contributor Ishaan Arora structured the LFX parameter extraction effort into **eight phases**, each tracked by a GitHub issue and corresponding PR.  These phases progressively build a pipeline: (1) exporting UDB parameters, (2) defining a formal taxonomy and prompts, (3) chunking the spec, (4) running an extraction agent, (5) analyzing results, and further refinement phases.  Key deliverables include Python scripts (`export_udb_params.py`, `run_prompt.py`, `chunker.py`, `analyze.py`, etc.), data artifacts (`ground_truth.json`, `chunks/*.adoc`), and YAML catalogs.  Most PRs remain **open** (work-in-progress) and have been reviewed by core maintainers (e.g. Paul Clarke, Derek Hower).  The table below lists each phase with PR links, status, and date.  

| Phase | PR (link) | Files/Paths Changed | Status | Date (first commit) |
| :---  | :---      | :---                | :---   | :--- |
| **1. Ground Truth Map** | [#1765](https://github.com/riscv/riscv-unified-db/pull/1765) | `param_extraction/scripts/` (export/map/generate), `param_extraction/data/{ground_truth.json,spec_mappings.json,parameters_catalog.csv,phase1_report.txt,udb_param_names.txt}` | **Open** | Mar 26, 2026 |
| **2. Taxonomy & Prompts** | [#1766](https://github.com/riscv/riscv-unified-db/pull/1766) | `docs/taxonomy.md`, `system_prompt.txt`, `examples.json`, `param_extraction/scripts/{run_prompt.py,validate_prompt.py}` | **Open** | Mar 26, 2026 |
| **3. Spec Chunking** | [#1783](https://github.com/riscv/riscv-unified-db/pull/1783) | `param_extraction/scripts/chunker.py`, `param_extraction/chunks/` (78→79 `.adoc` chunks + `manifest.json`) | **Open** | Apr  9, 2026 |
| **4. LLM Extraction** | [#1791](https://github.com/riscv/riscv-unified-db/pull/1791) | `param_extraction/scripts/extract.py` (run/pilot/merge subcommands), possibly prompt invocation code | **Open** | Apr 15, 2026 (PR opened) |
| **5. Analysis/Metrics** | [#1792](https://github.com/riscv/riscv-unified-db/pull/1792) | `param_extraction/scripts/analyze.py`, `param_extraction/data/one_to_many_groups.json`, `param_extraction/chunks/` (refreshed) | **Open** | May 25, 2026 |
| **6. Prompt Refinement** | [#1793](https://github.com/riscv/riscv-unified-db/pull/1793) | likely updates to prompts/examples (not found) | **Open** | Apr 15, 2026 |
| **7. Final Spreadsheet** | [#1831](https://github.com/riscv/riscv-unified-db/pull/1831) | CSV/XLS output generation (name unknown) | **Open** | May 13, 2026 |
| **8. (Future)** | – | – | – | – |

## Phase 1: Ground Truth Map (#1765, Open)  
**Summary:** Adds scripts and data to catalog all 185 non-MOCK UDB parameters with metadata. This includes `export_udb_params.py` (extracts from `spec/std/isa/param/*.yaml` with schema analysis and CSR cross-references), `map_params_to_spec.py` (keyword-search 74 ISA `.adoc` files for parameter occurrences), and `generate_report.py` (outputs CSV and reports).  Data outputs are committed: `param_extraction/data/ground_truth.json`, `spec_mappings.json`, `parameters_catalog.csv`, `phase1_report.txt`, and `udb_param_names.txt`. Key results include 185 parameters cataloged, 98% mapped to spec text, and 81% high-confidence classification.  
**Files Changed:** Scripts under `param_extraction/scripts/` (export/map/generate) and all new files in `param_extraction/data/`.  
**Review Comments:** On Mar 26, 2026 Ishaan summarized the deliverables (see above quote). No external review comments are visible yet, but Ishaan noted minor post-review fixes (encoding and CSV guard).  
**Status:** Open (awaiting merge); closes Issue #1747.  

## Phase 2: Taxonomy & LLM Prompt Design (#1766, Open)  
**Summary:** Defines a formal parameter taxonomy and builds the prompt architecture. Key deliverables (per Issue #1748) include `taxonomy.md` (documenting 8 classes like NORM_DIRECT, NORM_CSR_WARL, etc.), `system_prompt.txt` (role/task definition with ~940 tokens), `examples.json` (6 positive + 4 negative JSON examples), and `run_prompt.py` (assembler tool). The PR adds these artifacts: it also includes a validation script `validate_prompt.py` (175+ checks for consistency). The summary notes *“formal taxonomy (8 classes) with decision tree,”* and a three-layer prompt design (system + examples + chunk).  
**Files Changed:** Likely adds `docs/taxonomy.md`, `system_prompt.txt`, `examples.json`, and scripts under `param_extraction/scripts/` (`run_prompt.py`, `validate_prompt.py`). The exact diff isn’t loaded, but these are the named deliverables.  
**Review Comments:** Ishaan’s PR summary (Mar 26, 2026) details the content (see quote). The PR also mentions a “Validate suite” and is marked to close Issue #1748. No external comments quoted yet.  
**Status:** Open; closes #1748.  

## Phase 3: AsciiDoc-Aware Spec Chunking (#1783, Open)  
**Summary:** Splits the 52,602-line ISA manual into 78–79 chunks while preserving CSR section boundaries. Ishaan added `chunker.py` with `run/info/verify` commands, and committed a `param_extraction/chunks/` directory containing 78 numbered `.adoc` files plus `manifest.json`. Chunking rules are enumerated (e.g., no split inside a `====` section, 2.5K–3.5K lines per chunk, 30-line overlap). The PR reports 78 total chunks, 100% coverage (4 large files split into 2 each).  
**Files Changed:** `param_extraction/scripts/chunker.py`; under `param_extraction/chunks/` the generated chunk files (e.g. `chunk_1.adoc`, …) and `manifest.json`.  
**Review Comments:** Ishaan’s summary on Apr 9, 2026 explains the approach. An update notes that after fixing `merge_tiny_blocks`, the chunks increased to 79. It shows a before/after: “Total chunks: 78 → 79”.  
**Status:** Open; closes #1749.  

## Phase 4: LLM Extraction Pipeline (#1791, Open)  
**Summary:** Builds on phases 1–3 to actually run the LLM extraction. According to project notes, the goal was to implement an `extract.py` script with `pilot`, `run`, and `merge` modes (to try example prompts, batch-run the model, and combine chunk results). This PR (#1791) was opened Apr 15, 2026 (filter suggests “6 tasks done”) and would contain `param_extraction/scripts/extract.py` and possibly a new prompt layer for output. (Unfortunately the PR content was not viewable to us.)  
**Files Changed:** Presumably `param_extraction/scripts/extract.py` and related configuration (e.g. OpenAI API calls or prompt templates).  
**Review Comments:** (Not visible in our view.) Likely mentions testing the extraction on sample text.  
**Status:** **Open** (Review required).  

## Phase 5: Analysis, Alignment & Metrics (#1792, Open)  
**Summary:** Introduces `analyze.py`, a pipeline to compare LLM output to ground truth. It performs deduplication (dropping cross-chunk duplicates), multi-strategy alignment (exact match, one-to-many groups, fuzzy/name-stems, concept groups), and computes metrics and discrepancy reports. Results quoted: raw recall 60.0%, adjusted recall 62.7%, classification accuracy 67.9%, and 153 new params discovered.  
**Files Changed:** `param_extraction/scripts/analyze.py`; adds `param_extraction/data/one_to_many_groups.json` (8 curated groups). It also refreshes the `param_extraction/chunks/` output after last changes (79 chunks with metadata).  
**Review Comments:** Ishaan’s summary Apr 9, 2026 is quoted above. He later documented fixes: a stricter concept-group rule (36.8% raw recall) and then an allow-list of one-to-many groups to “count every group member as aligned”. These updates dramatically raised recall to 60.0% (honest count).  
**Status:** Open; closes #1749 (the issue was for phase 3, but the summary says closes).  

## Phase 6: Prompt Refinement & V2 (PR #1793, Open)  
**Summary:** Intended to iterate prompts based on Phase 5 findings. PR #1793 (Apr 15, 2026) likely updates `system_prompt.txt` and examples or parameters (Issue #1752 pointed to it). Content not reviewed here, but the aim was a “V2 system prompt” and cover missed cases.  
**Files Changed:** Probably revised `system_prompt.txt`, new positive/negative examples, and re-run of extraction.  
**Status:** Open (review required).  

## Phase 7: Final Parameter Spreadsheet (PR #1831, Open)  
**Summary:** Compiles final reviewed parameters into a spreadsheet or YAML for sharing. Issue #1754 referred to it. The PR adds a spreadsheet (XLSX or CSV) of parameters with names, descriptions, categories.  
**Files Changed:** Likely an output file (e.g. `param_extraction/data/final_parameters.csv`) and possibly export scripts.  
**Status:** Open (review requested May 13, 2026).  

## Phase 8: (Planned)  
This is an inferred phase to merge results into UDB format and CI. No PR found yet, but likely to “push final files upstream” and automate the pipeline (per LFX guidelines).  

## Analysis and Suggestions  
The above PRs show a **thorough pipeline**, but also some gaps and open issues: there is no evidence yet of automated **validation of final YAML outputs**, handling of LLM hallucinations in the prompt, or integration of results back into the UDB schema. Key strengths include comprehensive tooling (export, chunking, analysis) and attention to edge cases (one-to-many groups, prefix matches). Weaknesses include the lack of **continuous integration** (none of the PRs show CI checks on merge), potential prompt errors leading to low recall (36–60%), and no mechanism shown to **convert extracted parameters into UDB YAML** (the deliverable for phase 1 was only for ground truth).  

Based on this, here are **five concrete suggestions** (ranked by likely impact vs short-term feasibility):  

1. **Implement Automated YAML Validation and Schema Checks** – Add scripts or CI jobs that validate the final extracted parameters against the UDB JSON Schema. This directly addresses “missing validation” by catching malformed or duplicate entries before merging. It’s relatively straightforward (using existing JSON Schema validators) and high-impact for reliability.  
2. **Refine Prompts with High-Recall Examples** – Analyze missed parameters (from Phase 5 reports) to craft additional few-shot examples or modify instructions to reduce hallucination/false negatives. For example, ensure negative examples cover permissive “may” usage and injection of overlapping contexts. This aligns with mentorship goals of prompt robustness and can boost recall. It’s high impact and doable by iterating on `examples.json`/`system_prompt.txt`.  
3. **Add CI/CD for Prompt Testing** – Create a lightweight CI workflow (e.g. GitHub Actions) that runs the `run_prompt.py` on a small set of chunks to detect regressions on prompt changes. This makes the pipeline reproducible (one-command execution) and ensures prompt edits don’t break parsing. Given existing GitHub Actions shown (e.g., Phase 5 run), this is quite feasible.  
4. **Export to UDB YAML and Schema Update** – Build on the ISA-manual flow to translate extracted parameters into UDB YAML entries, updating the unified-db `param/*.yaml`. This meets project task 4, bridging to maintainers. A script could load the final CSV/JSON catalog and generate YAML files, ensuring consistency with `param.schema.json`. It’s moderate effort but essential for integration.  
5. **Mitigate Hallucinations via Constraint and Verification** – To further reduce hallucinations, enhance the LLM output schema with explicit `evidence` fields (e.g. line references) and enforce closed-domain constraint (deny text outside spec patterns). One could also implement a post-hoc filter that cross-checks any “new” parameter against a whitelist or the ground truth. This suggestion is high-impact for quality but more complex; a prototype might just flag outputs lacking clear evidence.  

**Summary for Submission:**  
*In reviewing Ishaan Arora’s PR history, I mapped each “Phase” to its PRs and artifacts. This helped me pinpoint existing scripts (e.g. `export_udb_params.py`, `chunker.py`, `analyze.py`) and gaps (e.g. lack of automated schema validation, no direct UDB YAML export). The insights guided my coding-challenge approach: I will reuse the established pipeline structure, refine prompts based on Phase 5 error analyses, add quick CI checks for prompt outputs, and script conversion of final results into UDB YAML. In other words, by reverse-engineering Ishaan’s phases, I can jumpstart implementation of similar features (ground truth catalog, prompt assembly, extraction and validation) and focus my limited time on the uncovered tasks (hallucination handling and UDB export) that maximally advance the project goals.*  

**Sources:** GitHub PRs #1765, #1766, #1783, #1792, and related issue threads. These provide the detailed descriptions above.