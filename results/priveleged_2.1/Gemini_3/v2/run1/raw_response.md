parameters: []

rejected:
  - candidate: CSR_ADDRESS_WIDTH
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]).
    explanation: >
      The 12-bit width of the CSR address is a fixed architectural constant.

  - candidate: CSR_TOTAL_COUNT
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      For up to 4,096 CSRs.
    explanation: >
      The maximum number of CSRs is fixed by the 12-bit address space.

  - candidate: CSR_ACCESS_CONTROL_BITS
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      The top two bits (csr[11:10]) indicate whether the register is
      read/write (00,01, or 10) or read-only (11).
    explanation: >
      The function of specific bits in the CSR address is defined by the ISA
      and is not implementation-specific.