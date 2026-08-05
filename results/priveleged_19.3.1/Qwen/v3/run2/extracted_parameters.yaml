parameters:
  - name: CACHE_BLOCK_SIZE
    long_name: Cache block size
    description: Implementation-defined size of a cache block.
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
    explanation: "The specification identifies cache capacity as implementation-specific but does not indicate that software-observable ISA behavior varies with this value."

  - candidate: CACHE_ORGANIZATION
    reason: NOT_ISA_VISIBLE
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    explanation: "Cache organization is described as an implementation detail without explicit ISA-visible architectural effects."

  - candidate: CACHE_BLOCK_SIZE_UNIFORMITY
    reason: CONSTRAINT_NOT_PARAMETER
    excerpt: "In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    explanation: "Uniformity is an architectural constraint imposed on the cache-block-size parameter rather than a configurable implementation parameter."