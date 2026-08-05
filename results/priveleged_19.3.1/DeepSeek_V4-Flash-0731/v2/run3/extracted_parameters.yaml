parameters:
  - name: CACHE_CAPACITY
    description: Implementation-selected cache capacity.
    type: integer
    constraints: {}
    excerpt: >
      The capacity and organization of a cache and the size of a cache block
      are both implementation-specific.
    trigger: implementation-specific
    confidence: high

  - name: CACHE_ORGANIZATION
    description: Implementation-selected cache organization.
    type: string
    constraints: {}
    excerpt: >
      The capacity and organization of a cache and the size of a cache block
      are both implementation-specific.
    trigger: implementation-specific
    confidence: high

  - name: CACHE_BLOCK_SIZE
    description: >
      Implementation-selected size of a cache block. Cache blocks are
      contiguous, naturally aligned power-of-two (NAPOT) memory ranges and
      remain uniform throughout the system.
    type: integer
    constraints:
      note: Must be power-of-two (or NAPOT)
    excerpt: >
      The capacity and organization of a cache and the size of a cache block
      are both implementation-specific. In the initial set of CMO extensions,
      the size of a cache block shall be uniform throughout the system.
    trigger: implementation-specific
    confidence: high

rejected: []