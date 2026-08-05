parameters: []

rejected:
  - candidate: CSR[11:10] encoding for read/write versus read-only accessibility
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11).
    explanation: The encoding of the upper CSR address bits is fixed by the ISA and cannot be selected by an implementation.

  - candidate: CSR[9:8] encoding for lowest privilege level
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR.
    explanation: The privilege-level encoding is architecturally defined and is not an implementation-configurable parameter.