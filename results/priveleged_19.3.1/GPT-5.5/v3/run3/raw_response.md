parameters:
  - name: CACHE_CAPACITY
    long_name: Cache Capacity
    description: Storage capacity of a cache selected by the implementation.
    type: integer
    constraints: {}
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    isa_visible: true
    confidence: high

  - name: CACHE_ORGANIZATION
    long_name: Cache Organization
    description: Structural organization of a cache selected by the implementation.
    type: string
    constraints: {}
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    isa_visible: true
    confidence: medium

  - name: CACHE_BLOCK_SIZE
    long_name: Cache Block Size
    description: Size of an implementation-defined cache block.
    type: integer
    constraints:
      note: "In the initial set of CMO extensions, the cache block size shall be uniform throughout the system."
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    isa_visible: true
    confidence: high

rejected:
  - candidate: CACHE_BLOCK_NAPOT_PROPERTY
    reason: CONSTRAINT_NOT_PARAMETER
    excerpt: "each of which represents a contiguous, naturally aligned power-of-two (or NAPOT) range of memory locations."
    explanation: "This is a mandatory architectural constraint describing cache blocks, not an implementation-selectable parameter."

  - candidate: CACHE_BLOCK_ADDRESS_IDENTIFICATION
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "A cache block is identified by any of the physical addresses corresponding to the underlying memory locations."
    explanation: "This specifies architectural behavior and does not permit implementation variation."

  - candidate: CACHE_INFORMATION_DISCOVERY_INTERFACE
    reason: NOT_STATED_IN_TEXT
    excerpt: "the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    explanation: "The specification mentions that software can discover cache information but does not define a configurable architectural parameter."