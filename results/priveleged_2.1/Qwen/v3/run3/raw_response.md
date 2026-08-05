parameters: []

rejected:
  - candidate: CSR_ADDRESS_WIDTH
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The width of the CSR address encoding space is fixed by the ISA specification."

  - candidate: CSR_COUNT
    reason: NOT_STATED_IN_TEXT
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The specification defines only the available encoding space and does not state that implementations select the number of CSRs."

  - candidate: CSR_ACCESSIBILITY_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "By convention, the upper 4 bits of the CSR address (csr[11:8]) are used to encode the read and write accessibility of the CSRs according to privilege level as shown in Table 1."
    explanation: "The placement and meaning of the accessibility encoding are fixed by the architectural specification."

  - candidate: CSR_READ_WRITE_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: "The read/write encoding associated with csr[11:10] is architecturally defined."

  - candidate: CSR_PRIVILEGE_LEVEL_ACCESS_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: "The privilege-level access encoding is fixed by the ISA and is not an implementation choice."