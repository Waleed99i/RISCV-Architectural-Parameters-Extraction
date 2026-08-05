parameters:
  - name: CACHE_CAPACITY
    long_name: Cache Capacity
    description: Implementation-defined total storage capacity of a cache.
    type: integer
    constraints: {}
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: specification
    isa_visible: true
    confidence: high

  - name: CACHE_ORGANIZATION
    long_name: Cache Organization
    description: Implementation-defined structural organization of a cache.
    type: string
    constraints: {}
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: specification
    isa_visible: true
    confidence: high

  - name: CACHE_BLOCK_SIZE
    long_name: Cache Block Size
    description: Implementation-defined cache block size represented as a contiguous, naturally aligned power-of-two (or NAPOT) memory range. The size is uniform throughout the system in the initial CMO extensions.
    type: integer
    constraints:
      note: "power-of-two (or NAPOT); uniform throughout the system"
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system. In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    trigger: implementation-specific
    defined_by: specification
    isa_visible: true
    confidence: high

rejected: []