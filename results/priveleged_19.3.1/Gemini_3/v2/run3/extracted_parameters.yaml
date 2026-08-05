parameters:
  - name: CACHE_CAPACITY
    description: Implementation-selected storage capacity of the cache.
    type: integer
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: null
    excerpt: >
      The capacity and organization of a cache and the size of a cache block
      are both implementation-specific.
    trigger: implementation-specific
    confidence: high

  - name: CACHE_ORGANIZATION
    description: Implementation-selected structural organization of the cache.
    type: string
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: null
    excerpt: >
      The capacity and organization of a cache and the size of a cache block
      are both implementation-specific.
    trigger: implementation-specific
    confidence: high

  - name: CACHE_BLOCK_SIZE
    description: Implementation-selected size of a cache block.
    type: integer
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: >
        Must be power-of-two, naturally aligned, and uniform across the
        system.
    excerpt: >
      The capacity and organization of a cache and the size of a cache block
      are both implementation-specific.
    trigger: implementation-specific
    confidence: high

rejected:
  - candidate: NAPOT_REQUIREMENT
    reason: CONSTRAINT_ONLY
    excerpt: >
      Naturally aligned power-of-two (or NAPOT) range.
    explanation: >
      This is a mandatory constraint on the CACHE_BLOCK_SIZE parameter rather
      than a separate parameter.