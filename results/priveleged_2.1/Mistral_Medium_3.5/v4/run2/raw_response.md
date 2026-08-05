parameters: []
rejected:


candidate: csr_address_mapping_convention
category: Architectural Constant
reason: FIXED_BY_ARCHITECTURE
excerpt: "By convention, the upper 4 bits of the CSR address (csr[11:8]) are used to encode the read and write accessibility of the CSRs according to privilege level as shown in Table 1."
explanation: The convention is fixed and not an implementation choice.


candidate: csr_read_only_encoding
category: Architectural Constant
reason: FIXED_BY_ARCHITECTURE
excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
explanation: The encoding for read-only vs. read/write is fixed by the architecture.