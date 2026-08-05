parameters:
  - name: CACHE_BLOCK_SIZE
    long_name: Cache Block Size
    description: Implementation-specific size of a cache block that is discoverable by software.
    type: integer
    constraints:
      - implementation-specific
      - discoverable by software
      - system-wide uniformity in the initial set of CMO extensions
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
    explanation: The passage identifies cache capacity as implementation-specific but does not explicitly state that architectural behavior depends on it.

  - candidate: CACHE_ORGANIZATION
    category: Microarchitectural Detail
    reason: NOT_ISA_VISIBLE
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific"
    explanation: Cache organization is implementation-specific, but the supplied text does not explicitly establish ISA-visible behavior.

  - candidate: CACHE_BLOCK_UNIFORMITY
    category: Architectural Constraint
    reason: CONSTRAINT_NOT_PARAMETER
    excerpt: "In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    explanation: This is a mandatory architectural requirement rather than an implementation-selected parameter.