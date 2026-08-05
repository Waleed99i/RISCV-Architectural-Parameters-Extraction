parameters: []

rejected:
  - candidate: CSR_ENCODING_SPACE
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The size of the CSR encoding space is fixed by the ISA specification and is not implementation-configurable."

  - candidate: CSR_ACCESSIBILITY_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: "The encoding of read/write and read-only CSR accessibility is mandated by the architecture."

  - candidate: CSR_PRIVILEGE_LEVEL_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: "The privilege-level encoding is prescribed by the RISC-V ISA and does not represent an implementation choice."