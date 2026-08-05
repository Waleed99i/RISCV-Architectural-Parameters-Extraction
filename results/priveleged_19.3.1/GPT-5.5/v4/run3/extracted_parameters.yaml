parameters:
  - name: CACHE_BLOCK_SIZE
    long_name: Cache Block Size
    description: Implementation-specific size of a cache block that software can discover through the execution environment.
    type: integer
    constraints:
      - implementation-specific
      - uniform throughout the system in the initial set of CMO extensions
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system. In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    trigger: implementation-specific
    defined_by: Snippet1
    isa_visible: true
    confidence: high

rejected:
  - candidate: CACHE_CAPACITY
    category: Microarchitectural Detail
    reason: NOT_ISA_VISIBLE
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    explanation: Although implementation-specific, the passage does not state that cache capacity changes ISA-visible architectural behavior.

  - candidate: CACHE_ORGANIZATION
    category: Microarchitectural Detail
    reason: NOT_ISA_VISIBLE
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    explanation: Cache organization is implementation-specific but is not identified as an ISA-visible architectural parameter.

  - candidate: CACHE_BLOCK_SIZE_UNIFORMITY
    category: Architectural Constraint
    reason: CONSTRAINT_NOT_PARAMETER
    excerpt: "In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    explanation: This sentence specifies a mandatory architectural constraint rather than a configurable implementation parameter.