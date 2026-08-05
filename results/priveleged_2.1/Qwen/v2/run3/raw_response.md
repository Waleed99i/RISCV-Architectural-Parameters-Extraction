parameters: []

rejected:
  - candidate: CSR_ADDRESS_WIDTH
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      12-bit encoding space (csr[11:0]).
    explanation: >
      The CSR address width is architecturally fixed.

  - candidate: CSR_COUNT
    reason: NOT_SUPPORTED_BY_TEXT
    excerpt: >
      up to 4,096 CSRs.
    explanation: >
      The snippet specifies the encoding capacity, not the number of CSRs
      implemented.

  - candidate: CSR_ACCESS_TYPE_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      The top two bits (csr[11:10]) indicate whether the register is
      read/write or read-only.
    explanation: >
      The bit assignments are fixed by the architecture.

  - candidate: CSR_LOWEST_PRIVILEGE_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      The next two bits (csr[9:8]) encode the lowest privilege level.
    explanation: >
      This encoding is defined by the ISA rather than selected by an
      implementation.