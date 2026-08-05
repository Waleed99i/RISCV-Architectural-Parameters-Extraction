parameters: []

rejected:
  - candidate: CSR_ADDRESS_ENCODING
    category: Architectural Constant
    reason: ARCHITECTURAL_CONSTANT
    excerpt: "a 12-bit encoding space (csr[11:0])"
    explanation: The CSR address encoding width is fixed by the ISA specification.

  - candidate: CSR_ACCESSIBILITY_MAPPING
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "By convention, the upper 4 bits of the CSR address (csr[11:8]) are used to encode the read and write accessibility"
    explanation: The accessibility mapping is architecturally specified and not implementation-selectable.

  - candidate: CSR_RW_PERMISSION_BITS
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: The encoding of read/write permissions is fixed by the architecture.

  - candidate: CSR_PRIVILEGE_LEVEL_BITS
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: The privilege-level encoding is architecturally fixed and does not represent an implementation-defined parameter.