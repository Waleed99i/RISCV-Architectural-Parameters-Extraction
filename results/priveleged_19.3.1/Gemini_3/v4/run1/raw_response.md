parameters:
  - name: CACHE_CAPACITY
    long_name: Cache Capacity
    description: The total storage capacity of the cache.
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
    description: The structural organization of the cache.
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
    description: The size of a cache block, representing a contiguous, naturally aligned power-of-two range of memory locations.
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
  - candidate: CACHE_BLOCK_IDENTIFICATION
    category: Descriptive Information
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "A cache block is identified by any of the physical addresses corresponding to the underlying memory locations."
    explanation: This defines how cache blocks are identified architecturally rather than an implementation-selectable parameter.

  - candidate: DISCOVERY_MEANS
    category: Descriptive Information
    reason: DESCRIPTIVE_TEXT
    excerpt: "the execution environment provides software a means to discover information about the caches and cache blocks in a system"
    explanation: This describes a capability of the execution environment instead of an architectural parameter.