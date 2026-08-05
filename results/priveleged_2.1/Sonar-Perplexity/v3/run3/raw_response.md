parameters:
  - name: csr_accessibility_encoding
    long_name: CSR accessibility and privilege encoding
    description: The upper bits of the CSR address specify read/write accessibility together with the minimum privilege level required to access the CSR.
    type: architectural encoding
    constraints:
      - csr[11:8] encodes CSR accessibility
      - csr[11:10] identifies read/write or read-only
      - csr[9:8] identifies the lowest privilege level
    excerpt: "By convention, the upper 4 bits of the CSR address (csr[11:8]) are used to encode the read and write accessibility of the CSRs according to privilege level as shown in Table 1."
    trigger: "By convention"
    defined_by: "Snippet2"
    isa_visible: true
    confidence: medium

rejected: []