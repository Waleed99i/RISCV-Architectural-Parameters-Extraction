parameters:
  - name: CACHE_BLOCK_SIZE
    long_name: Cache block size
    description: Implementation-selected size of a cache block.
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
    explanation: "Although implementation-specific, the passage does not explicitly establish cache capacity as an ISA-visible architectural parameter."

  - candidate: CACHE_ORGANIZATION
    reason: NOT_ISA_VISIBLE
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    explanation: "The specification identifies cache organization as implementation-specific but does not describe any ISA-visible behavior that depends on it."

  - candidate: CACHE_BLOCK_SIZE_UNIFORMITY
    reason: CONSTRAINT_NOT_PARAMETER
    excerpt: "In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    explanation: "Uniform cache-block size is a mandatory architectural constraint and therefore not a separate implementation-selected parameter."