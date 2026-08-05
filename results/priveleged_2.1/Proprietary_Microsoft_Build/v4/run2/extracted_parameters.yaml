parameters: []

rejected:
  - candidate: CSR_ENCODING_SPACE
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: The 12-bit CSR encoding space is fixed by the RISC-V ISA and is not implementation-configurable.

  - candidate: CSR_ACCESSIBILITY_ENCODING
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: The read/write versus read-only encoding is prescribed by the ISA and cannot be changed by implementations.

  - candidate: CSR_PRIVILEGE_LEVEL_ENCODING
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: The privilege-level encoding for CSR accessibility is architecturally defined and is not an implementation parameter.