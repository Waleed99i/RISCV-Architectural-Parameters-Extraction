parameters: []

rejected:
  - candidate: "csr_encoding_space"
    category: "Architectural Constant"
    reason: "ARCHITECTURAL_CONSTANT"
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The width of the CSR encoding space is fixed by the RISC-V ISA specification and is not implementation-configurable."

  - candidate: "csr_address_bit_mapping"
    category: "Architectural Constant"
    reason: "ARCHITECTURAL_CONSTANT"
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11). The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: "The allocation of CSR address bits for access permissions and privilege levels is architecturally defined and therefore not an implementation parameter."