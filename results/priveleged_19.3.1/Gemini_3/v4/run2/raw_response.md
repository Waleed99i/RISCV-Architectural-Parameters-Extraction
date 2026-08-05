parameters:
  - name: CACHE_CAPACITY
    long_name: Cache Capacity
    description: The implementation-defined capacity of a cache.
    type: integer
    constraints:
      - implementation-specific
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: implementation
    isa_visible: true
    confidence: high

  - name: CACHE_ORGANIZATION
    long_name: Cache Organization
    description: The implementation-defined organization of the cache.
    type: string
    constraints:
      - implementation-specific
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: implementation
    isa_visible: true
    confidence: high

  - name: CACHE_BLOCK_SIZE
    long_name: Cache Block Size
    description: The implementation-defined size of a cache block corresponding to a contiguous, naturally aligned NAPOT memory region.
    type: integer
    constraints:
      - implementation-specific
      - contiguous
      - naturally aligned
      - power-of-two
      - NAPOT
      - uniform throughout the system
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: implementation
    isa_visible: true
    confidence: high

rejected:
  - candidate: CACHE_BLOCK_IDENTIFIER
    category: Descriptive Information
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "A cache block is identified by any of the physical addresses corresponding to the underlying memory locations."
    explanation: The statement specifies the architectural identification method for cache blocks rather than an implementation-selectable parameter.

  - candidate: CACHE_DISCOVERY_INTERFACE
    category: Descriptive Information
    reason: DESCRIPTIVE_TEXT
    excerpt: "the execution environment provides software a means to discover information about the caches and cache blocks in a system"
    explanation: This describes functionality supplied by the execution environment rather than a configurable architectural parameter.