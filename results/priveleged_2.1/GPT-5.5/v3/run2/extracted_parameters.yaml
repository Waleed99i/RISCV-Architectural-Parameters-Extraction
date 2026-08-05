parameters: []

rejected:
  - candidate: CSR_ENCODING_SPACE_WIDTH
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The width of the CSR encoding space is fixed by the ISA."

  - candidate: CSR_ADDRESS_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "By convention, the upper 4 bits of the CSR address (csr[11:8]) are used to encode the read and write accessibility of the CSRs according to privilege level as shown in Table 1."
    explanation: "The assignment of the upper CSR address bits is architecturally defined."

  - candidate: CSR_READ_ONLY_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: "The read/write and read-only encodings are fixed by the ISA."

  - candidate: CSR_PRIVILEGE_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: "The privilege-level encoding is specified by the architecture."

  - candidate: CSR_IMPLEMENTATION_COUNT
    reason: NOT_STATED_IN_TEXT
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The passage specifies the encoding capacity but does not state that implementations may choose how many CSRs to implement."