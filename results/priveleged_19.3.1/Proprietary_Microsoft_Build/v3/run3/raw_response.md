parameters:
  - name: CACHE_CAPACITY
    long_name: Cache Capacity
    description: The cache capacity is implementation-specific.
    type: integer
    constraints: {}
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: specification
    isa_visible: true
    confidence: high

  - name: CACHE_ORGANIZATION
    long_name: Cache Organization
    description: The cache organization is implementation-specific.
    type: string
    constraints: {}
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: specification
    isa_visible: true
    confidence: high

  - name: CACHE_BLOCK_SIZE
    long_name: Cache Block Size
    description: The size of a cache block is implementation-specific and is required to be uniform throughout the system for the initial CMO extensions.
    type: integer
    constraints:
      note: "power-of-two (or NAPOT); uniform throughout the system in the initial CMO extensions"
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system. In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    trigger: implementation-specific
    defined_by: specification
    isa_visible: true
    confidence: high

rejected: []