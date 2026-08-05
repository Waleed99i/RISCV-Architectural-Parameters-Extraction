parameters: []

rejected:
  - candidate: "CSR[11:10] encoding for read/write vs read-only accessibility"
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: "The interpretation of csr[11:10] is fixed by the ISA specification and is not configurable by implementations."

  - candidate: "CSR[9:8] encoding for the lowest privilege level"
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: "The assignment of csr[9:8] to privilege-level encoding is defined by the architecture and is not implementation-dependent."