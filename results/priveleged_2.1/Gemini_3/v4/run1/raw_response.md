parameters: []

rejected:
  - candidate: CSR_ADDRESS_WIDTH
    category: Architectural Constant
    reason: ARCHITECTURAL_CONSTANT
    excerpt: "a 12-bit encoding space (csr[11:0])"
    explanation: The width of the CSR address encoding is fixed by the ISA specification.

  - candidate: CSR_MAX_COUNT
    category: Architectural Constant
    reason: ARCHITECTURAL_CONSTANT
    excerpt: "for up to 4,096 CSRs"
    explanation: The maximum CSR count follows directly from the architecturally defined 12-bit encoding space.

  - candidate: CSR_ACCESS_CONVENTION
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "the upper 4 bits of the CSR address (csr[11:8]) are used to encode the read and write accessibility"
    explanation: The encoding of CSR accessibility is fixed by the ISA and is not implementation-configurable.

  - candidate: CSR_PRIVILEGE_MAPPING
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: The privilege-level encoding of CSR address bits is architecturally specified rather than implementation-defined.