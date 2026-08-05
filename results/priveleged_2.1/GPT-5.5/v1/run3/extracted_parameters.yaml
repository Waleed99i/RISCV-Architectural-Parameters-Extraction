parameters:
  - name: CSR_ADDRESS_WIDTH
    description: Width of the CSR encoding space.
    type: integer
    constraints:
      - "12 bits"

  - name: CSR_ADDRESS_SPACE_SIZE
    description: Number of CSR encodings in the CSR encoding space.
    type: integer
    constraints:
      - maximum: 4096

  - name: CSR_ACCESS_TYPE_ENCODING
    description: Encoding of CSR read/write accessibility.
    type: enum
    constraints:
      - "00: read/write"
      - "01: read/write"
      - "10: read/write"
      - "11: read-only"

  - name: CSR_LOWEST_PRIVILEGE_LEVEL_ENCODING
    description: Encoding of the lowest privilege level that can access a CSR.
    type: enum
    constraints: []