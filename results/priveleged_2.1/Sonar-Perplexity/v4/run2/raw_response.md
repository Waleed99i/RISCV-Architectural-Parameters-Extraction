parameters: []

rejected:
  - candidate: csr_accessibility_encoding
    category: Descriptive Information
    reason: NOT_STATED_IN_TEXT
    excerpt: "\"Conventional\" R/W accessibility of CSRs according to address mapping"
    explanation: The snippet describes CSR address mapping but does not identify an implementation-configurable parameter.

  - candidate: csr[11:0] encoding space
    category: Architectural Constant
    reason: ARCHITECTURAL_CONSTANT
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: The CSR address width is fixed by the architecture.

  - candidate: csr[11:8] accessibility encoding
    category: Architectural Constant
    reason: ARCHITECTURAL_CONSTANT
    excerpt: "By convention, the upper 4 bits of the CSR address (csr[11:8]) are used to encode the read and write accessibility of the CSRs according to privilege level as shown in Table 1."
    explanation: The bit mapping is architecturally fixed.

  - candidate: csr[11:10] read/write or read-only encoding
    category: Architectural Constant
    reason: ARCHITECTURAL_CONSTANT
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: The encoding values are fixed by the ISA.

  - candidate: csr[9:8] lowest privilege level encoding
    category: Architectural Constant
    reason: ARCHITECTURAL_CONSTANT
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: The privilege encoding is fixed by the ISA.