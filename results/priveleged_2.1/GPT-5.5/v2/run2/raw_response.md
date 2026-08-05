parameters: []

rejected:
  - candidate: CSR_ADDRESS_WIDTH
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "12-bit encoding space"
    explanation: Defined by the ISA.

  - candidate: CSR_ENCODING_SPACE
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "up to 4,096 CSRs"
    explanation: Determined directly from the fixed encoding.

  - candidate: CSR_RW_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "00,01,10 ... 11"
    explanation: Architecturally fixed encoding.

  - candidate: CSR_PRIVILEGE_BITS
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "csr[9:8]"
    explanation: Architecturally fixed field assignment.