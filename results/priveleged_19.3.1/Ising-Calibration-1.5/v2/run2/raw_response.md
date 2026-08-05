parameters:
  - name: CACHE_BLOCK_SIZE
    description: Implementation-selected size of a cache block.
    type: integer
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: Naturally aligned power-of-two (NAPOT); uniform throughout the system.
    excerpt: >
      The size of a cache block is implementation-specific... In the initial
      set of CMO extensions, the size of a cache block shall be uniform
      throughout the system.
    trigger: implementation-specific
    confidence: high

  - name: CACHE_CAPACITY
    description: Implementation-selected capacity of the cache.
    type: integer
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: null
    excerpt: >
      The capacity ... is implementation-specific.
    trigger: implementation-specific
    confidence: medium

rejected: []