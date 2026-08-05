parameters: []
rejected:
  - candidate: csr_encoding_space_size
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: The size of the CSR encoding space is fixed by the standard RISC-V ISA and is not an implementation choice.
  - candidate: csr_rw_accessibility_encoding
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: The encoding of read/write accessibility is fixed by convention in the standard RISC-V ISA.
  - candidate: csr_privilege_level_encoding
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: The encoding of the lowest privilege level is fixed by convention in the standard RISC-V ISA