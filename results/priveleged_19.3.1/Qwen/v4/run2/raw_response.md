parameters:
  - name: "CACHE_BLOCK_SIZE"
    long_name: "Cache block size"
    description: "Implementation-specific size of a cache block."
    type: "integer"
    constraints:
      - "implementation-specific"
      - "discoverable"
      - "power-of-two"
      - "naturally aligned"
      - "In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    excerpt: "Caches organize copies of data into cache blocks, each of which represents a contiguous, naturally aligned power-of-two (or NAPOT) range of memory locations. A cache block is identified by any of the physical addresses corresponding to the underlying memory locations. The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system. In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    trigger: "implementation-specific"
    defined_by: "implementation"
    isa_visible: true
    confidence: "medium"

rejected:
  - candidate: "CACHE_CAPACITY"
    category: "Microarchitectural Detail"
    reason: "NOT_ISA_VISIBLE"
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    explanation: "The text states that cache capacity is implementation-specific, but it does not explicitly state that software observes this value through ISA-visible architectural behaviour."

  - candidate: "CACHE_ORGANIZATION"
    category: "Microarchitectural Detail"
    reason: "NOT_ISA_VISIBLE"
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    explanation: "The text states that cache organization is implementation-specific, but it does not explicitly state that software observes this value through ISA-visible architectural behaviour."

  - candidate: "CACHE_BLOCK_SIZE_UNIFORMITY"
    category: "Architectural Constraint"
    reason: "CONSTRAINT_NOT_PARAMETER"
    excerpt: "In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    explanation: "This is a mandatory architectural constraint and not an implementation-selected parameter."

  - candidate: "CACHE_BLOCK_RANGE_PROPERTY"
    category: "Architectural Constraint"
    reason: "CONSTRAINT_NOT_PARAMETER"
    excerpt: "Caches organize copies of data into cache blocks, each of which represents a contiguous, naturally aligned power-of-two (or NAPOT) range of memory locations."
    explanation: "This describes required properties of cache blocks rather than an implementation-configurable parameter."