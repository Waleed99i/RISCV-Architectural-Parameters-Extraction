parameters: []

rejected:
  - candidate: CSR_ADDRESS_WIDTH
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "12-bit encoding space"
    explanation: The width is fixed by the ISA.

  - candidate: CSR_COUNT
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "up to 4,096 CSRs"
    explanation: This is an architectural consequence of the fixed encoding width.

  - candidate: CSR_ACCESS_TYPE_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "00,01,10 ... 11"
    explanation: The encoding is fixed by the ISA.

  - candidate: CSR_PRIVILEGE_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "csr[9:8]"
    explanation: The privilege encoding is fixed by the ISA.