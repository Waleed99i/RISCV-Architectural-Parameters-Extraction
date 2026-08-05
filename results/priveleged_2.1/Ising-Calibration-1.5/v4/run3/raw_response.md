parameters: []

rejected:
  - candidate: CSRAddressWidth
    category: ARCHITECTURAL_CONSTANT
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
    explanation: The CSR address width is fixed by the RISC-V ISA and is not configurable by implementations.

  - candidate: PrivilegeLevelEncoding
    category: ARCHITECTURAL_CONSTANT
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "By convention, the upper 4 bits of the CSR address (csr[11:8]) are used to encode the read and write accessibility of the CSRs according to privilege level as shown in Table 1."
    explanation: The encoding of privilege and access permissions is prescribed by the ISA and does not represent an implementation-defined parameter.