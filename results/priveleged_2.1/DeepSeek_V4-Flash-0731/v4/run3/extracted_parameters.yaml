parameters: []

rejected:
  - candidate: CSR[11:10] read/write accessibility encoding
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11).
    explanation: The read/write accessibility encoding is fixed by the architectural specification and is not implementation-configurable.

  - candidate: CSR[9:8] lowest privilege level encoding
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR.
    explanation: The privilege-level encoding is prescribed by the architecture and does not represent an implementation-defined parameter.