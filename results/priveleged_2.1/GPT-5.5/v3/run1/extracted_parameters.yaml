parameters: []

rejected:
  - candidate: CSR_ADDRESS_WIDTH
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The CSR address width is fixed by the ISA."

  - candidate: CSR_ADDRESS_SPACE_SIZE
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The encoding space is architecturally fixed."

  - candidate: CSR_ACCESS_TYPE_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: "The encoding of read/write versus read-only CSRs is fixed by the ISA."

  - candidate: CSR_PRIVILEGE_LEVEL_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: "The privilege-level encoding is architecturally specified."

  - candidate: CSR_ADDRESS_MAPPING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "By convention, the upper 4 bits of the CSR address (csr[11:8]) are used to encode the read and write accessibility of the CSRs according to privilege level"
    explanation: "The mapping of CSR address bits is fixed by the architecture."