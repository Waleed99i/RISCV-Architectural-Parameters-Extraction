parameters:
  - name: CACHE_CAPACITY
    long_name: Cache Capacity
    description: Capacity of a cache.
    type: integer
    constraints: {}
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    isa_visible: true
    confidence: high

  - name: CACHE_ORGANIZATION
    long_name: Cache Organization
    description: Organization of a cache.
    type: string
    constraints: {}
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    isa_visible: true
    confidence: high

  - name: CACHE_BLOCK_SIZE
    long_name: Cache Block Size
    description: Size of a cache block.
    type: integer
    constraints:
      note: "In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    isa_visible: true
    confidence: high

rejected:
  - candidate: CACHE_BLOCK_ALIGNMENT
    reason: CONSTRAINT_NOT_PARAMETER
    excerpt: "each of which represents a contiguous, naturally aligned power-of-two (or NAPOT) range of memory locations."
    explanation: "This specifies a required property of cache blocks rather than an implementation-selectable parameter."

  - candidate: CACHE_BLOCK_IDENTIFIER
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "A cache block is identified by any of the physical addresses corresponding to the underlying memory locations."
    explanation: "This defines architectural behavior rather than implementation freedom."

  - candidate: CACHE_INFORMATION_DISCOVERY
    reason: NOT_STATED_IN_TEXT
    excerpt: "the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    explanation: "The text requires a discovery mechanism but does not define an implementation-configurable parameter."