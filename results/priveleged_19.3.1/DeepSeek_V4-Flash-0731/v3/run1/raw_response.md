parameters:
  - name: CACHE_CAPACITY
    long_name: Cache Capacity
    description: The total capacity of a cache is implementation-specific.
    type: integer
    constraints: {}
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific..."
    trigger: "implementation-specific"
    defined_by: specification
    isa_visible: true
    confidence: high

  - name: CACHE_ORGANIZATION
    long_name: Cache Organization
    description: The organization of a cache is implementation-specific.
    type: string
    constraints: {}
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific..."
    trigger: "implementation-specific"
    defined_by: specification
    isa_visible: true
    confidence: high

  - name: CACHE_BLOCK_SIZE
    long_name: Cache Block Size
    description: The size of a cache block is implementation-specific but must be uniform throughout the system.
    type: integer
    constraints:
      note: "Uniform across the system"
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific... In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    trigger: "implementation-specific"
    defined_by: specification
    isa_visible: true
    confidence: high

rejected: []