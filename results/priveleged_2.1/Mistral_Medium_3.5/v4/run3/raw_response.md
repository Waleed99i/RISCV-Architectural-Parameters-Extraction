parameters: []
rejected:


candidate: csr_privilege_level_encoding
category: Architectural Constant
reason: FIXED_BY_ARCHITECTURE
excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
explanation: The encoding for privilege levels is fixed by the architecture.


candidate: csr_encoding_space_size
category: Architectural Constant
reason: FIXED_BY_ARCHITECTURE
excerpt: "The standard RISC-V ISA sets aside a 12-bit encoding space (csr[11:0]) for up to 4,096 CSRs."
explanation: The size of the encoding space is fixed and not configurable.