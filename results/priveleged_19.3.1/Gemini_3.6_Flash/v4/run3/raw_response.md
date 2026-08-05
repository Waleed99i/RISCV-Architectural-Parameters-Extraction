parameters:
  - name: "cache_block_size"
    long_name: "Cache Block Size"
    description: "Implementation-specific cache block size representing a contiguous, naturally aligned power-of-two (NAPOT) memory region."
    type: "integer"
    constraints:
      alignment: "naturally aligned"
      power_of_two: true
      system_wide_requirement: "uniform throughout the system"
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system. In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    trigger: "implementation-specific"
    defined_by: "implementation"
    isa_visible: true
    confidence: "high"

rejected:
  - candidate: "cache_capacity"
    category: "Microarchitectural Detail"
    reason: "MICROARCHITECTURAL_DETAIL"
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    explanation: "Cache capacity is an implementation-specific hardware characteristic that does not directly affect ISA-visible architectural behavior."

  - candidate: "cache_organization"
    category: "Microarchitectural Detail"
    reason: "MICROARCHITECTURAL_DETAIL"
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    explanation: "Cache organization is a microarchitectural implementation detail and is not directly observable through the ISA."