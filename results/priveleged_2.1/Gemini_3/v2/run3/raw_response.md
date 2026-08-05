parameters: []

rejected:
  - candidate: CSR_PRIVILEGE_MAPPING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      The next two bits (csr[9:8]) encode the lowest privilege level that can
      access the CSR.
    explanation: >
      This is a fixed bitfield definition within the RISC-V CSR address space.

  - candidate: CSR_RW_MAPPING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      Upper 4 bits of the CSR address (csr[11:8]) are used to encode the read
      and write accessibility.
    explanation: >
      These address bit mappings are architectural constants, not choices for
      the implementation.