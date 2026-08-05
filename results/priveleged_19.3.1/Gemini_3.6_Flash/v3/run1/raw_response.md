parameters:
  - name: "cache_block_size"
    long_name: "Cache Block Size"
    description: "The size of a cache block in bytes, representing a contiguous, naturally aligned power-of-two (NAPOT) range of memory locations."
    type: "integer"
    constraints:
      minimum: null
      maximum: null
      enum: null
      note: "Must be a naturally aligned power-of-two (or NAPOT) range of memory locations and uniform throughout the system."
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system. In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    trigger: "implementation-specific"
    defined_by: "implementation"
    isa_visible: true
    confidence: "high"

rejected:
  - candidate: "cache_capacity"
    reason: "NOT_ISA_VISIBLE"
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    explanation: "Cache capacity is microarchitectural and does not alter ISA-visible instruction execution behavior or register state."

  - candidate: "cache_organization"
    reason: "NOT_ISA_VISIBLE"
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    explanation: "Cache organization parameters such as associativity are microarchitectural details not visible to software through the ISA."