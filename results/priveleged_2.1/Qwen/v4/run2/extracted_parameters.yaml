parameters: []

rejected:
  - candidate: "CSR_ADDRESS_WIDTH"
    category: "Architectural Constant"
    reason: "FIXED_BY_ARCHITECTURE"
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The CSR address width is fixed by the architecture and cannot be selected by an implementation."

  - candidate: "MAX_CSR_COUNT"
    category: "Architectural Constant"
    reason: "FIXED_BY_ARCHITECTURE"
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The maximum CSR count is derived from the fixed architectural encoding space."

  - candidate: "CSR_ACCESSIBILITY_ENCODING"
    category: "Architectural Constant"
    reason: "FIXED_BY_ARCHITECTURE"
    excerpt: "By convention, the upper 4 bits of the CSR address (csr[11:8]) are used to encode the read and write accessibility of the CSRs according to privilege level as shown in Table 1."
    explanation: "The CSR accessibility mapping is defined by the architecture and is not implementation-selected."

  - candidate: "CSR_READ_WRITE_ENCODING"
    category: "Architectural Constant"
    reason: "FIXED_BY_ARCHITECTURE"
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: "The read/write encoding is fixed by the architecture."

  - candidate: "CSR_PRIVILEGE_LEVEL_ACCESS_ENCODING"
    category: "Architectural Constant"
    reason: "FIXED_BY_ARCHITECTURE"
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: "The privilege-level encoding is fixed by the architecture."