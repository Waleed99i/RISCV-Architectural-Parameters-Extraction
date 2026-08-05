parameters:
  - name: CACHE_BLOCK_SIZE
    long_name: Cache block size
    description: Implementation-specific size of a cache block.
    type: integer
    constraints: []
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: implementation-specific
    defined_by: implementation
    isa_visible: true
    confidence: medium

rejected:
  - candidate: CACHE_CAPACITY
    reason: NOT_ISA_VISIBLE
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    explanation: "The passage states that cache capacity is implementation-specific, but it does not explicitly state that ISA-visible behavior depends on this value."

  - candidate: CACHE_ORGANIZATION
    reason: NOT_ISA_VISIBLE
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    explanation: "Although implementation-specific, cache organization is presented as a microarchitectural property rather than an ISA-visible architectural parameter."

  - candidate: CACHE_BLOCK_SIZE_UNIFORMITY
    reason: CONSTRAINT_NOT_PARAMETER
    excerpt: "In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    explanation: "This sentence specifies a mandatory architectural requirement on cache-block size rather than introducing a separate implementation-selected parameter."