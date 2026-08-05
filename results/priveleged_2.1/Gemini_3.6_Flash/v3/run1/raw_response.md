parameters: []

rejected:
  - candidate: "csr_encoding_space"
    reason: "FIXED_BY_ARCHITECTURE"
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The 12-bit CSR address encoding space is an architectural constant defined by the specification."

  - candidate: "csr_address_bit_mapping"
    reason: "FIXED_BY_ARCHITECTURE"
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11). The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: "The mapping of CSR address bits to privilege levels and read/write permissions is fixed by the RISC-V architecture."