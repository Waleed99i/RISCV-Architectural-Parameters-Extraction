parameters: []

rejected:
  - candidate: CSR_ADDRESS_WIDTH
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      The standard RISC-V ISA sets aside a 12-bit encoding space
      (csr[11:0]) for up to 4,096 CSRs.
    explanation: >
      The CSR address width is fixed by the ISA and is not an
      implementation-selected parameter.

  - candidate: PRIVILEGE_LEVEL_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      The upper 4 bits of the CSR address are used to encode read/write
      accessibility according to privilege level.
    explanation: >
      The encoding of privilege level and accessibility is defined by the
      ISA and cannot vary between implementations.