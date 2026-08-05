parameters: []

rejected:
  - candidate: CSR_ADDRESS_SPACE_WIDTH
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]).
    explanation: >
      The CSR address width is specified by the architecture and is not
      configurable.

  - candidate: CSR_PRIVILEGE_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      The next two bits (csr[9:8]) encode the lowest privilege level.
    explanation: >
      The privilege encoding is architecturally defined and therefore is not
      an implementation parameter.