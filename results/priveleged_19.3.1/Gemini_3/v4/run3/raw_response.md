parameters:
  - name: CACHE_CAPACITY
    long_name: Cache Capacity
    description: Implementation-defined storage capacity of a cache.
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
    description: Implementation-defined organization of the cache.
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
    description: Implementation-defined cache block size representing a contiguous, naturally aligned power-of-two (NAPOT) memory region.
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
  - candidate: CACHE_DATA_LAYOUT
    category: Descriptive Information
    reason: DESCRIPTIVE_TEXT
    excerpt: "Caches organize copies of data into cache blocks"
    explanation: This sentence describes the function of caches and does not define a configurable architectural parameter.

  - candidate: CACHE_BLOCK_ADDRESSING
    category: Descriptive Information
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "A cache block is identified by any of the physical addresses corresponding to the underlying memory locations."
    explanation: This defines the architectural method for identifying cache blocks rather than an implementation-defined parameter.