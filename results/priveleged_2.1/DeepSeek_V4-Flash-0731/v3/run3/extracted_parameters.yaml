parameters: []

rejected:
  - candidate: CSR_ENCODING_SPACE
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The 12-bit CSR encoding space is defined by the ISA and is not an implementation-selected parameter."

  - candidate: CSR_ACCESSIBILITY_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: "The accessibility encoding of CSR address bits is fixed by the architecture and cannot vary across compliant implementations."

  - candidate: CSR_PRIVILEGE_LEVEL_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: "The privilege-level encoding is prescribed by the RISC-V ISA and therefore is not an implementation-specific architectural parameter."