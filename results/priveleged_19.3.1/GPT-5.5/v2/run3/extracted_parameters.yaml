parameters:
  - name: CACHE_CAPACITY
    description: Capacity of a cache.
    type: integer
    constraints:
      note: implementation-specific
    excerpt: "The capacity ... implementation-specific"
    trigger: implementation-specific
    confidence: high

  - name: CACHE_ORGANIZATION
    description: Organization of a cache.
    type: string
    constraints:
      note: implementation-specific
    excerpt: "organization ... implementation-specific"
    trigger: implementation-specific
    confidence: high

  - name: CACHE_BLOCK_SIZE
    description: Size of a cache block.
    type: integer
    constraints:
      note: implementation-specific; uniform throughout the system in the initial set of CMO extensions
    excerpt: "size of a cache block ... implementation-specific"
    trigger: implementation-specific
    confidence: high

rejected:
  - candidate: CACHE_BLOCK_NAPOT
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "power-of-two (or NAPOT)"
    explanation: This specifies the architectural definition of a cache block.

  - candidate: CACHE_BLOCK_PHYSICAL_ADDRESS
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "identified by any of the physical addresses"
    explanation: This is architectural behavior.

  - candidate: CACHE_INFORMATION_DISCOVERY
    reason: MANDATORY_REQUIREMENT
    excerpt: "execution environment provides software a means to discover"
    explanation: This is an execution-environment requirement rather than an implementation parameter.