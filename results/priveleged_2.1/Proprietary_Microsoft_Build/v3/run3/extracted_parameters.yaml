parameters: []

rejected:
  - candidate: "CSR[11:10] encoding for read/write vs read-only accessibility"
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The top two bits (csr[11:10]) indicate whether the register is read/write (00,01, or 10) or read-only (11)."
    explanation: "The encoding of csr[11:10] is prescribed by the RISC-V ISA and therefore is not an implementation-selectable parameter."

  - candidate: "CSR[9:8] encoding for the lowest privilege level"
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "The next two bits (csr[9:8]) encode the lowest privilege level that can access the CSR."
    explanation: "The privilege-level encoding assigned to csr[9:8] is fixed by the architecture and cannot vary across compliant implementations."