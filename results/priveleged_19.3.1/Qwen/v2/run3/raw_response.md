parameters:
  - name: CACHE_CAPACITY
    description: Cache capacity.
    type: integer
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: implementation-specific
    excerpt: >
      The capacity and organization of a cache... are both
      implementation-specific.
    trigger: implementation-specific
    confidence: high

  - name: CACHE_ORGANIZATION
    description: Organization of a cache.
    type: string
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: implementation-specific
    excerpt: >
      The capacity and organization of a cache... are both
      implementation-specific.
    trigger: implementation-specific
    confidence: medium

  - name: CACHE_BLOCK_SIZE
    description: Cache block size.
    type: integer
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: >
        Implementation-specific. Uniform throughout the system for the
        initial CMO extensions.
    excerpt: >
      The size of a cache block is implementation-specific... the size of a
      cache block shall be uniform throughout the system.
    trigger: implementation-specific
    confidence: high

rejected:
  - candidate: CACHE_BLOCK_IDENTIFIER
    reason: FIXED_BY_ARCHITECTURE
    excerpt: >
      A cache block is identified by any of the physical addresses.
    explanation: >
      This specifies architectural behavior instead of implementation
      freedom.