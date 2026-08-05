parameters:
  - name: CACHE_CAPACITY
    long_name: Cache Capacity
    description: Total storage capacity of a cache selected by the implementation.
    type: integer
    constraints: {}
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific..."
    trigger: "implementation-specific"
    defined_by: specification
    isa_visible: true
    confidence: high

  - name: CACHE_ORGANIZATION
    long_name: Cache Organization
    description: Cache organization is implementation-specific.
    type: string
    constraints: {}
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific..."
    trigger: "implementation-specific"
    defined_by: specification
    isa_visible: true
    confidence: high

  - name: CACHE_BLOCK_SIZE
    long_name: Cache Block Size
    description: Cache block size is implementation-specific and required to be uniform throughout the system.
    type: integer
    constraints:
      note: "Uniform throughout the system in the initial set of CMO extensions."
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific... In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    trigger: "implementation-specific"
    defined_by: specification
    isa_visible: true
    confidence: high

rejected: []