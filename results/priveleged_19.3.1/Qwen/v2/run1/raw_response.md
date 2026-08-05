parameters:
  - name: CACHE_CAPACITY
    description: Capacity of a cache.
    type: integer
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: null
    excerpt: >
      The capacity and organization of a cache and the size of a cache
      block are both implementation-specific.
    trigger: implementation-specific
    confidence: high

  - name: CACHE_ORGANIZATION
    description: Organization of a cache.
    type: string
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: null
    excerpt: >
      The capacity and organization of a cache and the size of a cache
      block are both implementation-specific.
    trigger: implementation-specific
    confidence: medium

  - name: CACHE_BLOCK_SIZE
    description: Size of a cache block.
    type: integer
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: >
        Cache blocks are contiguous, naturally aligned power-of-two (or
        NAPOT) ranges. In the initial set of CMO extensions, cache-block
        size is uniform throughout the system.
    excerpt: >
      The capacity and organization of a cache and the size of a cache
      block are both implementation-specific, and the execution
      environment provides software a means to discover information about
      the caches and cache blocks in a system. In the initial set of CMO
      extensions, the size of a cache block shall be uniform throughout
      the system.
    trigger: implementation-specific
    confidence: high

rejected:
  - candidate: CACHE_BLOCK_SIZE_UNIFORMITY
    reason: MANDATORY_REQUIREMENT
    excerpt: >
      In the initial set of CMO extensions, the size of a cache block
      shall be uniform throughout the system.
    explanation: >
      Uniform cache-block size is required for the initial set of CMO
      extensions, so it is not an implementation choice.