parameters:
  - name: "cache_block_size"
    long_name: "Cache Block Size"
    description: "Implementation-selected size of a cache block representing a contiguous, naturally aligned power-of-two (NAPOT) region of memory."
    type: "integer"
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: "Cache block size shall be uniform throughout the system in the initial set of CMO extensions."
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system. In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    trigger: "implementation-specific"
    defined_by: "implementation"
    isa_visible: true
    confidence: "high"

rejected:
  - candidate: "cache_capacity"
    reason: "NOT_ISA_VISIBLE"
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    explanation: "Although implementation-specific, cache capacity is a microarchitectural characteristic and is not directly observable through the ISA."

  - candidate: "cache_organization"
    reason: "NOT_ISA_VISIBLE"
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    explanation: "Properties such as cache associativity or organization influence implementation but are not ISA-visible architectural parameters."