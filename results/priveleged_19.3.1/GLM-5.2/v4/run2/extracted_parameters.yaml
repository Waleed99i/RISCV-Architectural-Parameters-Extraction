parameters:
  - name: cache_capacity
    long_name: Cache capacity
    description: The capacity of a cache, which is implementation-specific and discoverable by software.
    type: unspecified
    constraints:
      - implementation-specific
      - discoverable
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: implementation-specific
    defined_by: Unspecified
    isa_visible: true
    confidence: high
  - name: cache_organization
    long_name: Cache organization
    description: The organization of a cache, which is implementation-specific and discoverable by software.
    type: unspecified
    constraints:
      - implementation-specific
      - discoverable
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: implementation-specific
    defined_by: Unspecified
    isa_visible: true
    confidence: high
  - name: cache_block_size
    long_name: Cache block size
    description: The size of a cache block, which is implementation-specific and discoverable by software.
    type: integer
    constraints:
      - contiguous
      - naturally aligned
      - power-of-two (or NAPOT)
      - uniform throughout the system
      - implementation-specific
      - discoverable
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: implementation-specific
    defined_by: Unspecified
    isa_visible: true
    confidence: high
rejected:
  - candidate: uniform_cache_block_size
    category: Architectural Constraint
    reason: CONSTRAINT_NOT_PARAMETER
    excerpt: "In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    explanation: The text mandates that the cache block size shall be uniform, which acts as an architectural constraint rather than an implementation-configurable parameter.
  - candidate: cache_information_discovery_mechanism
    category: Descriptive Information
    reason: DESCRIPTIVE_TEXT
    excerpt: "the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    explanation: The text describes a feature of the execution environment rather than an implementation-configurable architectural parameter