parameters:
  - name: CACHE_CAPACITY
    description: Capacity of a cache.
    type: integer
    constraints:
      note: implementation-specific
    excerpt: "The capacity and organization of a cache ... are both implementation-specific"
    trigger: implementation-specific
    confidence: high

  - name: CACHE_ORGANIZATION
    description: Organization of a cache.
    type: string
    constraints:
      note: implementation-specific
    excerpt: "The capacity and organization of a cache ... are both implementation-specific"
    trigger: implementation-specific
    confidence: high

  - name: CACHE_BLOCK_SIZE
    description: Size of a cache block.
    type: integer
    constraints:
      note: implementation-specific; shall be uniform throughout the system in the initial set of CMO extensions
    excerpt: "the size of a cache block are both implementation-specific ... the size of a cache block shall be uniform throughout the system"
    trigger: implementation-specific
    confidence: high

rejected:
  - candidate: CACHE_BLOCK_ALIGNMENT
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "naturally aligned power-of-two (or NAPOT)"
    explanation: The alignment requirement is fixed by the ISA rather than chosen by implementations.

  - candidate: CACHE_BLOCK_ADDRESSING
    reason: FIXED_BY_ARCHITECTURE
    excerpt: "A cache block is identified by any of the physical addresses..."
    explanation: This specifies architectural behavior rather than an implementation-selected parameter.

  - candidate: CACHE_INFORMATION_DISCOVERY
    reason: MANDATORY_REQUIREMENT
    excerpt: "the execution environment provides software a means to discover information"
    explanation: This is a requirement on the execution environment, not an implementation parameter.