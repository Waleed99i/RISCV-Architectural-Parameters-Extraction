parameters: []

rejected:
  - candidate: CSR_ENCODING_SPACE
    category: Architectural Constant
    reason: ARCHITECTURAL_CONSTANT
    excerpt: "a 12-bit encoding space (csr[11:0])"
    explanation: The CSR encoding width is fixed by the architecture.

  - candidate: MAX_CSR_COUNT
    category: Architectural Constant
    reason: ARCHITECTURAL_CONSTANT
    excerpt: "for up to 4,096 CSRs"
    explanation: The maximum number of CSR encodings is determined by the fixed architectural address space.

  - candidate: CSR_RW_ACCESS_ENCODING
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: The read/write accessibility encoding is fixed by the ISA specification.

  - candidate: CSR_PRIVILEGE_ENCODING
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: The privilege-level encoding of CSR address bits is architecturally defined and not implementation-selectable.