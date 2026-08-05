parameters:
  - name: csr_accessibility_encoding
    long_name: CSR accessibility encoding
    description: The CSR address uses upper address bits to encode accessibility and the minimum privilege level required for access.
    type: architectural encoding
    constraints:
      - csr[11:8] contains accessibility information
      - csr[11:10] specifies read/write or read-only
      - csr[9:8] specifies the lowest privilege level
    excerpt: "By convention, the upper 4 bits of the CSR address (csr[11:8]) are used to encode the read and write accessibility of the CSRs according to privilege level as shown in Table 1."
    trigger: "By convention"
    defined_by: "Snippet2"
    isa_visible: true
    confidence: medium

rejected: []