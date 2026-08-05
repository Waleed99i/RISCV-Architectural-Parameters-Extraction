parameters: []

rejected:
  - candidate: "csr_encoding_space"
    reason: "FIXED_BY_ARCHITECTURE"
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: "The width of the CSR encoding space is fixed by the RISC-V ISA specification and cannot vary across implementations."

  - candidate: "csr_access_encoding"
    reason: "FIXED_BY_ARCHITECTURE"
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11). The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: "The assignment of CSR address bits for access permissions and privilege levels is architecturally defined rather than implementation-selectable."