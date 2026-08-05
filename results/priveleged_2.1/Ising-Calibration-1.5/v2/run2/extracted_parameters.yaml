parameters: []

rejected:
  - candidate: CSR_ENCODING_WIDTH
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]).
    explanation: >
      The CSR encoding width is architecturally fixed.

  - candidate: CSR_ACCESS_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      The top two bits indicate read/write or read-only and the next two bits
      encode the lowest privilege level.
    explanation: >
      These bit assignments are fixed by the ISA rather than chosen by an
      implementation.