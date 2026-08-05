parameters: []
rejected:
  - candidate: CSR_ENCODING_SPACE
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: The CSR encoding space is architecturally fixed at 12 bits and not implementation-selected.

  - candidate: CSR_ACCESSIBILITY_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: The accessibility encoding is defined by the ISA convention and not an implementation choice.

  - candidate: CSR_PRIVILEGE_LEVEL_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: Privilege level encoding is architecturally defined and not implementation-specific.