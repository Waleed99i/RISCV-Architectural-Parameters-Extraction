parameters: []

rejected:
  - candidate: >
      CSR encoding field layout (top two bits for read/write vs read-only,
      next two bits for privilege level)
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      The top two bits (csr[11:10]) indicate whether the register is
      read/write (00,01, or 10) or read-only (11). The next two bits
      (csr[9:8]) encode the lowest privilege level that can access the CSR.
    explanation: >
      The mapping of CSR address bits to accessibility and privilege level
      is architecturally fixed; no implementation choice exists.