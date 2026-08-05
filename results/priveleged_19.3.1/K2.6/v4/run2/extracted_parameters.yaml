parameters:
  - name: cache_capacity
    long_name: Cache Capacity
    description: The storage capacity of a cache.
    type: integer
    constraints:
      - implementation-specific
      - discoverable
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: implementation-specific
    defined_by: Snippet 1
    isa_visible: true
    confidence: high

  - name: cache_organization
    long_name: Cache Organization
    description: The internal organization of a cache.
    type: string
    constraints:
      - implementation-specific
      - discoverable
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: implementation-specific
    defined_by: Snippet 1
    isa_visible: true
    confidence: high

  - name: cache_block_size
    long_name: Cache Block Size
    description: The implementation-defined size of an individual cache block.
    type: integer
    constraints:
      - implementation-specific
      - discoverable
      - power-of-two
      - naturally aligned
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: implementation-specific
    defined_by: Snippet 1
    isa_visible: true
    confidence: high

rejected:
  - candidate: cache_block_uniformity
    category: Architectural Constraint
    reason: CONSTRAINT_NOT_PARAMETER
    excerpt: "In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    explanation: This specifies a mandatory system-wide requirement rather than an implementation-selectable architectural parameter.