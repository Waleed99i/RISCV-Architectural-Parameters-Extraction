parameters:
  - name: CACHE_CAPACITY
    description: Capacity of a cache.
    type: integer
    constraints: {}
    excerpt: >
      The capacity and organization of a cache and the size of a cache block
      are both implementation-specific.
    trigger: implementation-specific
    confidence: high

  - name: CACHE_ORGANIZATION
    description: Organization of a cache.
    type: string
    constraints: {}
    excerpt: >
      The capacity and organization of a cache and the size of a cache block
      are both implementation-specific.
    trigger: implementation-specific
    confidence: high

  - name: CACHE_BLOCK_SIZE
    description: >
      Size of a cache block, represented as a contiguous, naturally aligned
      power-of-two (or NAPOT) range of memory locations. Uniform throughout
      the system.
    type: integer
    constraints:
      note: Must be a power-of-two (or NAPOT)
    excerpt: >
      The capacity and organization of a cache and the size of a cache block
      are both implementation-specific. In the initial set of CMO extensions,
      the size of a cache block shall be uniform throughout the system.
    trigger: implementation-specific
    confidence: high

rejected: []