parameters: []

rejected:
  - candidate: csr_address_space
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: The 12-bit CSR address space is fixed by the RISC-V ISA specification.

  - candidate: csr_accessibility_encoding
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "By convention, the upper 4 bits of the CSR address (csr[11:8]) are used to encode the read and write accessibility of the CSRs according to privilege level as shown in Table 1."
    explanation: The CSR accessibility encoding is architecturally defined and is not implementation-configurable.

  - candidate: csr_read_write_indicator
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: The encoding for read/write versus read-only CSRs is fixed by the ISA.

  - candidate: csr_privilege_level_encoding
    category: Architectural Constant
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: The privilege-level encoding of CSR addresses is architecturally fixed and is not an implementation parameter.