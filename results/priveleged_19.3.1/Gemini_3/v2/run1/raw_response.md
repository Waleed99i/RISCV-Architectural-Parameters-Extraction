parameters:
  - name: CACHE_CAPACITY
    description: The total size or capacity of a cache.
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
    description: The structural organization (e.g., associativity, sets) of a cache.
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
    description: The size of a cache block in bytes.
    type: integer
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: >
        Must be a naturally aligned power-of-two (NAPOT) and uniform
        throughout the system in CMO extensions.
    excerpt: >
      The capacity and organization of a cache and the size of a cache block
      are both implementation-specific. In the initial set of CMO extensions,
      the size of a cache block shall be uniform throughout the system.
    trigger: implementation-specific
    confidence: high

rejected:
  - candidate: CACHE_BLOCK_ALIGNMENT
    reason: CONSTRAINT_ONLY
    excerpt: >
      Represents a contiguous, naturally aligned power-of-two (or NAPOT)
      range of memory locations.
    explanation: >
      Natural alignment is a mandatory property of how cache blocks represent
      memory, not an independent implementation parameter.