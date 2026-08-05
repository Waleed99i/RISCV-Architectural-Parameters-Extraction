parameters: []

rejected:
  - candidate: CSR[11:10] encoding for read/write vs read-only accessibility
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11).
    explanation: The mapping of these bits to accessibility is architecturally fixed and does not permit implementation choice.

  - candidate: CSR[9:8] encoding for the lowest privilege level
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR.
    explanation: The encoding of these bits to privilege level is architecturally fixed and does not permit implementation choice.