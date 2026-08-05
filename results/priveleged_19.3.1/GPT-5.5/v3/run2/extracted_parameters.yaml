parameters:
  - name: CACHE_CAPACITY
    long_name: Cache Capacity
    description: Implementation-selected capacity of a cache.
    type: integer
    constraints: {}
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    isa_visible: true
    confidence: high

  - name: CACHE_ORGANIZATION
    long_name: Cache Organization
    description: Implementation-selected organization of a cache.
    type: string
    constraints: {}
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    isa_visible: true
    confidence: medium

  - name: CACHE_BLOCK_SIZE
    long_name: Cache Block Size
    description: Implementation-selected size of a cache block.
    type: integer
    constraints:
      note: "The size of a cache block shall be uniform throughout the system in the initial set of CMO extensions."
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    isa_visible: true
    confidence: high

rejected:
  - candidate: CACHE_BLOCK_MEMORY_RANGE
    reason: CONSTRAINT_NOT_PARAMETER
    excerpt: "each of which represents a contiguous, naturally aligned power-of-two (or NAPOT) range of memory locations."
    explanation: "This describes a required property of a cache block rather than an implementation-selected parameter."

  - candidate: CACHE_BLOCK_IDENTIFICATION
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "A cache block is identified by any of the physical addresses corresponding to the underlying memory locations."
    explanation: "The identification rule is defined by the architecture and is not implementation configurable."

  - candidate: CACHE_DISCOVERY_MECHANISM
    reason: NOT_STATED_IN_TEXT
    excerpt: "the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    explanation: "The passage states that a discovery mechanism exists but does not define any configurable architectural parameter."