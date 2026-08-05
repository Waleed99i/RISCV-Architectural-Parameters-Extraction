parameters: []

rejected:
  - candidate: CSR_ADDRESS_ENCODING_WIDTH
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The CSR encoding width is fixed by the RISC-V ISA and cannot vary between implementations."

  - candidate: CSR_ACCESSIBILITY_BIT_MAPPING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "By convention, the upper 4 bits of the CSR address (csr[11:8]) are used to encode the read and write accessibility of the CSRs according to privilege level as shown in Table 1."
    explanation: "The assignment of CSR address bits to accessibility information is architecturally defined."

  - candidate: CSR_READ_WRITE_FIELD
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: "The meaning of these address bits is fixed by the architecture."

  - candidate: CSR_MINIMUM_PRIVILEGE_FIELD
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: "The encoding of the minimum privilege level is prescribed by the ISA and is not implementation-selectable."

  - candidate: NUMBER_OF_IMPLEMENTED_CSRS
    reason: NOT_STATED_IN_TEXT
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The text specifies the size of the encoding space but does not state that the number of implemented CSRs is an implementation parameter."