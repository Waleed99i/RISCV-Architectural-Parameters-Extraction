parameters:
  - name: csr_accessibility_encoding
    long_name: CSR access and privilege accessibility encoding
    description: The upper bits of a CSR address encode read/write accessibility and the lowest privilege level that can access the CSR.
    type: architectural encoding
    constraints:
      - csr[11:8] encodes accessibility by privilege level
      - csr[11:10] indicates read/write or read-only
      - csr[9:8] encodes the lowest privilege level that can access the CSR
    excerpt: "By convention, the upper 4 bits of the CSR address (csr[11:8]) are used to encode the read and write accessibility of the CSRs according to privilege level as shown in Table 1."
    trigger: "By convention"
    defined_by: "Snippet2"
    isa_visible: true
    confidence: medium

rejected: []