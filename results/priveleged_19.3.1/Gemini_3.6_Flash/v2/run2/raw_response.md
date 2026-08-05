parameters:

    name: "cache_block_size"
    description: "The size of a cache block in bytes, which represents a contiguous, naturally aligned power-of-two range of memory locations and is uniform throughout the system."
    type: "integer"
    constraints:
    minimum: null
    maximum: null
    enum: null
    note: "Must be a power-of-two (NAPOT) and uniform throughout the system."
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system. In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    trigger: "implementation-specific"
    confidence: "high"
    rejected:

    candidate: "cache_capacity"
    reason: "NOT_ISA_VISIBLE"
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    explanation: "Cache capacity is a microarchitectural property that does not directly alter instruction execution behavior or architectural state."

    candidate: "cache_organization"
    reason: "NOT_ISA_VISIBLE"
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    explanation: "Cache organization (e.g., associativity and set structure) is microarchitectural and not visible through standard ISA behavior."