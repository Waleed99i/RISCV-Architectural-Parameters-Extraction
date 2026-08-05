parameters:
  - name: CACHE_CAPACITY
    description: Total capacity of a cache.
    type: integer
    constraints: {}
    excerpt: >
      The capacity and organization of a cache and the size of a cache block
      are both implementation-specific.
    trigger: implementation-specific
    confidence: high

  - name: CACHE_ORGANIZATION
    description: Organization of the cache.
    type: string
    constraints: {}
    excerpt: >
      The capacity and organization of a cache and the size of a cache block
      are both implementation-specific.
    trigger: implementation-specific
    confidence: high

  - name: CACHE_BLOCK_SIZE
    description: >
      Implementation-selected cache block size. Cache blocks represent
      contiguous, naturally aligned power-of-two (NAPOT) memory ranges and
      are uniform throughout the system.
    type: integer
    constraints:
      note: Power-of-two (or NAPOT); uniform throughout the system
    excerpt: >
      The capacity and organization of a cache and the size of a cache block
      are both implementation-specific. In the initial set of CMO extensions,
      the size of a cache block shall be uniform throughout the system.
    trigger: implementation-specific
    confidence: high

rejected: []