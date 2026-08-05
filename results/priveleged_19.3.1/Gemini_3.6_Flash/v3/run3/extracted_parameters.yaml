parameters:
  - name: "cache_block_size"
    long_name: "Cache Block Size"
    description: "Implementation-defined size of a cache block corresponding to a contiguous, naturally aligned power-of-two (NAPOT) memory region."
    type: "integer"
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: "The cache block size shall be uniform throughout the system in the initial set of CMO extensions."
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system. In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    trigger: "implementation-specific"
    defined_by: "implementation"
    isa_visible: true
    confidence: "high"

rejected:
  - candidate: "cache_capacity"
    reason: "NOT_ISA_VISIBLE"
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    explanation: "Cache capacity is an implementation-specific microarchitectural property that is not directly visible through the architectural ISA interface."

  - candidate: "cache_organization"
    reason: "NOT_ISA_VISIBLE"
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    explanation: "Implementation details such as cache organization affect hardware design but do not change architecturally observable ISA behavior."