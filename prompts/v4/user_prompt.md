# User Prompt

You are given a snippet from the RISC-V ISA Manual.

Your task is to extract every architectural parameter that is explicitly supported by the provided text.

Follow the extraction pipeline defined in the system prompt.

Requirements

- Extract only implementation-defined or implementation-configurable architectural parameters.
- Every accepted parameter must include an exact supporting excerpt.
- Reject unsupported candidates rather than guessing.
- Do not use external knowledge.
- Produce deterministic output.

Return only valid YAML matching the expected output schema.

Specification Snippet

```text
<PASTE SPECIFICATION SNIPPET HERE>
```