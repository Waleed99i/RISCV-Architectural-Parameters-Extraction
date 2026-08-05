parameters:
  - name: CacheBlockSize
    long_name: Cache Block Size
    description: Implementation-defined cache block size representing the unit of cache allocation and transfer.
    type: integer
    constraints:
      implementation-specific: true
      power-of-two: true
      uniform: true
      minimum: 8
      maximum: 4096
      note: The cache block size follows a power-of-two (NAPOT) format and is required to be uniform across the system for the initial CMO extensions.
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: implementation-specific
    defined_by: RISC-V Cache Management Operations (CMO) Extension
    isa_visible: true
    confidence: high

  - name: CacheCapacity
    long_name: Cache Capacity
    description: Implementation-defined amount of storage available in a cache.
    type: integer
    constraints:
      implementation-specific: true
      minimum: 128
      maximum: 16777216
      note: Capacity depends on the particular cache implementation.
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: implementation-specific
    defined_by: RISC-V Cache Management Operations (CMO) Extension
    isa_visible: true
    confidence: high

rejected: []