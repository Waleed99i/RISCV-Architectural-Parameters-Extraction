parameters: []

rejected:
  - candidate: >
      CSR field encoding for access permissions and privilege level
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      The top two bits (csr[11:10]) indicate whether the register is
      read/write (00,01, or 10) or read-only (11). The next two bits
      (csr[9:8]) encode the lowest privilege level that can access the CSR.
    explanation: >
      The encoding of CSR address fields is prescribed by the architecture
      and does not represent implementation freedom.