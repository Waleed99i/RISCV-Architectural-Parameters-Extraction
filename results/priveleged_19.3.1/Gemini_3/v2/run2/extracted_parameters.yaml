parameters:
  - name: CACHE_CAPACITY
    description: The total capacity of the cache.
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
    description: The organizational structure of the cache.
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
    description: The size of a single cache block.
    type: integer
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: >
        Must be a power-of-two and naturally aligned. Must be uniform
        throughout the system.
    excerpt: >
      The capacity and organization of a cache and the size of a cache block
      are both implementation-specific.
    trigger: implementation-specific
    confidence: high

rejected:
  - candidate: DISCOVERY_MECHANISM
    reason: NOT_SUPPORTED_BY_TEXT
    excerpt: >
      The execution environment provides software a means to discover
      information.
    explanation: >
      The text mentions that a means is provided by the execution environment,
      but it does not specify an implementation-configurable parameter for the
      core itself.