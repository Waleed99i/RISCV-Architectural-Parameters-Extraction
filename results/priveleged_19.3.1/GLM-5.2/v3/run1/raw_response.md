parameters:
  - name: cache_capacity
    long_name: Cache capacity
    description: The capacity of a cache, which is implementation-specific and discoverable by software.
    type: integer
    constraints: Not specified in text.
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: Unspecified
    isa_visible: true
    confidence: high
  - name: cache_organization
    long_name: Cache organization
    description: The organization of a cache, which is implementation-specific and discoverable by software.
    type: unspecified
    constraints: Not specified in text.
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: Unspecified
    isa_visible: true
    confidence: high
  - name: cache_block_size
    long_name: Cache block size
    description: The size of a cache block, which is implementation-specific and discoverable by software.
    type: integer
    constraints: Represents a contiguous, naturally aligned power-of-two (or NAPOT) range of memory locations. Shall be uniform throughout the system in the initial set of CMO extensions.
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    trigger: implementation-specific
    defined_by: Unspecified
    isa_visible: true
    confidence: high
rejected:
  - candidate: cache_block_size_uniformity
    reason: CONSTRAINT_NOT_PARAMETER
    excerpt: "In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    explanation: The text mandates that the cache block size shall be uniform, which acts as an architectural constraint rather than an implementation-configurable parameter.