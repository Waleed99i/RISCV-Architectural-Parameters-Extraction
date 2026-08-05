parameters:
  - name: cache_block_size
    long_name: cache block size
    description: The size of a cache block is implementation-specific and the execution environment provides software a means to discover information about the caches and cache blocks in a system.
    type: Architectural Parameter
    constraints:
      - implementation-specific
      - discoverable
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: "the size of a cache block are both implementation-specific"
    defined_by: Snippet1
    isa_visible: true
    confidence: high

  - name: cache_capacity
    long_name: cache capacity
    description: The capacity of a cache is implementation-specific and software can discover information about caches and cache blocks in the system.
    type: Architectural Parameter
    constraints:
      - implementation-specific
      - discoverable
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: "The capacity and organization of a cache"
    defined_by: Snippet1
    isa_visible: true
    confidence: medium

  - name: cache_organization
    long_name: cache organization
    description: The organization of a cache is implementation-specific and software can discover information about caches and cache blocks in the system.
    type: Architectural Parameter
    constraints:
      - implementation-specific
      - discoverable
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: "The capacity and organization of a cache"
    defined_by: Snippet1
    isa_visible: true
    confidence: medium

rejected:
  - candidate: cache_block_uniformity
    category: Architectural Constraint
    reason: CONSTRAINT_NOT_PARAMETER
    excerpt: "In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    explanation: The text describes a mandatory system-wide requirement rather than an implementation-selected parameter.

  - candidate: cache_block_range_properties
    category: Architectural Constraint
    reason: CONSTRAINT_NOT_PARAMETER
    excerpt: "Caches organize copies of data into cache blocks, each of which represents a contiguous, naturally aligned power-of-two (or NAPOT) range of memory locations."
    explanation: The text defines properties of cache blocks but does not define an independent implementation-configurable parameter.