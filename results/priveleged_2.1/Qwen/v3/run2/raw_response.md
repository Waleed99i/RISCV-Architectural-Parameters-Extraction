parameters: []

rejected:
  - candidate: CSR_ADDRESS_WIDTH
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The 12-bit CSR address field is defined by the ISA and cannot be changed by an implementation."

  - candidate: CSR_COUNT
    reason: NOT_STATED_IN_TEXT
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The text specifies only the available encoding space and does not describe an implementation-selected CSR count."

  - candidate: CSR_ACCESSIBILITY_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "By convention, the upper 4 bits of the CSR address (csr[11:8]) are used to encode the read and write accessibility of the CSRs according to privilege level as shown in Table 1."
    explanation: "The encoding of CSR accessibility is architecturally prescribed and not implementation-configurable."

  - candidate: CSR_READ_WRITE_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: "The interpretation of csr[11:10] is fixed by the architectural definition."

  - candidate: CSR_PRIVILEGE_LEVEL_ACCESS_ENCODING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: "The privilege-level encoding assigned to csr[9:8] is mandated by the ISA and is not implementation-selectable."