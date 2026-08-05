parameters: []

rejected:
  - candidate: csr_encoding_space
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: The encoding space is fixed by the architecture and not configurable by the implementation.

  - candidate: csr_accessibility_mapping
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "By convention, the upper 4 bits of the CSR address (csr[11:8]) are used to encode the read and write accessibility of the CSRs according to privilege level as shown in Table 1."
    explanation: The mapping of accessibility bits is a fixed convention, not an implementation choice.

  - candidate: csr_read_write_bits
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: The encoding of read/write accessibility is fixed by the architecture.

  - candidate: csr_privilege_level_bits
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: The encoding of privilege level accessibility is fixed by the architecture.