parameters:
  - name: CacheBlockSize
    long_name: Cache Block Size
    description: Implementation-specific size of a cache block used for cache storage and transfers.
    type: integer
    constraints:
      implementation-specific: true
      power-of-two: true
      uniform: true
      minimum: 8
      maximum: 4096
      note: Cache blocks are power-of-two (or NAPOT) sized and must be uniform throughout the system for the initial CMO extensions.
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: implementation-specific
    defined_by: RISC-V Cache Management Operations (CMO) Extension
    isa_visible: true
    confidence: high

  - name: CacheCapacity
    long_name: Cache Capacity
    description: Implementation-specific total capacity of a cache.
    type: integer
    constraints:
      implementation-specific: true
      minimum: 128
      maximum: 16777216
      note: Cache capacity varies across implementations and cache hierarchy levels.
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: implementation-specific
    defined_by: RISC-V Cache Management Operations (CMO) Extension
    isa_visible: true
    confidence: high

rejected: []