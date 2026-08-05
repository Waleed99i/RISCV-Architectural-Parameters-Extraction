parameters:
  - name: CACHE_CAPACITY
    description: Capacity of a cache.
    type: integer
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: implementation-specific
    excerpt: >
      The capacity and organization of a cache and the size of a cache block
      are both implementation-specific.
    trigger: implementation-specific
    confidence: high

  - name: CACHE_ORGANIZATION
    description: Cache organization.
    type: string
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: implementation-specific
    excerpt: >
      The capacity and organization of a cache and the size of a cache block
      are both implementation-specific.
    trigger: implementation-specific
    confidence: high

  - name: CACHE_BLOCK_SIZE
    description: Size of a cache block.
    type: integer
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: >
        Implementation-specific. Shall be uniform throughout the system in
        the initial set of CMO extensions.
    excerpt: >
      The capacity and organization of a cache and the size of a cache block
      are both implementation-specific... the size of a cache block shall be
      uniform throughout the system.
    trigger: implementation-specific
    confidence: high

rejected:
  - candidate: CACHE_BLOCK_ALIGNMENT
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      naturally aligned power-of-two (or NAPOT) range
    explanation: >
      This defines the architectural properties of a cache block rather than
      an implementation-selected parameter.