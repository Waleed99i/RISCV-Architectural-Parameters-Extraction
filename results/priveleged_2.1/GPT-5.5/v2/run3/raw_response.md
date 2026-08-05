parameters: []

rejected:
  - candidate: CSR_ADDRESS_WIDTH
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "12-bit encoding space"
    explanation: The encoding width is fixed by the ISA.

  - candidate: CSR_ADDRESS_LAYOUT
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "csr[11:8]"
    explanation: The field layout is fixed by the ISA.

  - candidate: CSR_RW_ACCESS_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "00,01,10 ... 11"
    explanation: The access encoding is fixed.

  - candidate: CSR_PRIVILEGE_LEVEL_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "csr[9:8]"
    explanation: The privilege encoding is architecturally defined.