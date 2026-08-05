parameters: []

rejected:
  - candidate: CSR_ADDRESS_WIDTH
    category: Architectural Constant
    reason: ARCHITECTURAL_CONSTANT
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: The CSR address width is fixed by the ISA specification.

  - candidate: CSR_ENCODING_SPACE
    category: Architectural Constant
    reason: ARCHITECTURAL_CONSTANT
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: The encoding space is defined by the architecture and is not implementation-configurable.

  - candidate: CSR_ACCESSIBILITY_BIT_MAPPING
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "By convention, the upper 4 bits of the CSR address (csr[11:8]) are used to encode the read and write accessibility of the CSRs according to privilege level as shown in Table 1."
    explanation: The mapping of the upper CSR address bits is prescribed by the architecture.

  - candidate: CSR_READ_ONLY_ENCODING
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: The encoding of read/write versus read-only registers is architecturally fixed.

  - candidate: CSR_PRIVILEGE_ENCODING
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: The privilege-level encoding is fixed by the ISA and does not represent an implementation choice.