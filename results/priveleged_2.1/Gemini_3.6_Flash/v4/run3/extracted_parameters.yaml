parameters: []

rejected:
  - candidate: "csr_encoding_space"
    category: "Architectural Constant"
    reason: "ARCHITECTURAL_CONSTANT"
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The CSR encoding space is fixed by the architectural specification and cannot vary between implementations."

  - candidate: "csr_address_bit_mapping"
    category: "Architectural Constant"
    reason: "ARCHITECTURAL_CONSTANT"
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11). The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: "The interpretation of the CSR address bits is defined by the ISA and is not an implementation-selectable architectural parameter."