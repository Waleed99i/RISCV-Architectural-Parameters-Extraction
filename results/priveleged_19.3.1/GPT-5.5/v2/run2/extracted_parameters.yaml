parameters:
  - name: CACHE_CAPACITY
    description: Cache capacity.
    type: integer
    constraints:
      note: implementation-specific
    excerpt: "capacity ... implementation-specific"
    trigger: implementation-specific
    confidence: high

  - name: CACHE_ORGANIZATION
    description: Cache organization.
    type: string
    constraints:
      note: implementation-specific
    excerpt: "organization ... implementation-specific"
    trigger: implementation-specific
    confidence: high

  - name: CACHE_BLOCK_SIZE
    description: Cache block size.
    type: integer
    constraints:
      note: implementation-specific; uniform throughout the system in the initial set of CMO extensions
    excerpt: "size of a cache block ... implementation-specific"
    trigger: implementation-specific
    confidence: high

rejected:
  - candidate: CACHE_BLOCK_RANGE
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "power-of-two (or NAPOT) range"
    explanation: The range description defines the architecture rather than an implementation choice.

  - candidate: CACHE_BLOCK_IDENTIFIER
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "identified by any of the physical addresses"
    explanation: This defines architectural semantics.

  - candidate: CACHE_DISCOVERY_INTERFACE
    reason: MANDATORY_REQUIREMENT
    excerpt: "execution environment provides software a means to discover"
    explanation: This is a requirement, not an implementation-selected property.