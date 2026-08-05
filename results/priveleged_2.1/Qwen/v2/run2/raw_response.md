parameters: []

rejected:
  - candidate: CSR_ADDRESS_WIDTH
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      The standard RISC-V ISA sets aside a 12-bit encoding space.
    explanation: >
      The width of the CSR address space is fixed by the ISA.

  - candidate: CSR_ADDRESS_SPACE
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      up to 4,096 CSRs.
    explanation: >
      This follows directly from the fixed encoding space rather than an
      implementation choice.

  - candidate: CSR_RW_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      00, 01, or 10 indicate read/write and 11 indicates read-only.
    explanation: >
      These encodings are architecturally specified.

  - candidate: CSR_PRIVILEGE_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      The next two bits (csr[9:8]) encode the lowest privilege level.
    explanation: >
      The encoding is fixed by the ISA.