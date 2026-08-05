parameters: []

rejected:
  - candidate: "csr_encoding_space"
    reason: "FIXED_BY_ARCHITECTURE"
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The 12-bit CSR encoding space is specified by the ISA and is therefore not an implementation-configurable architectural parameter."

  - candidate: "csr_address_bit_mapping"
    reason: "FIXED_BY_ARCHITECTURE"
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11). The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: "The assignment of CSR address bits to read/write permissions and privilege levels is mandated by the RISC-V architecture and cannot vary across compliant implementations."