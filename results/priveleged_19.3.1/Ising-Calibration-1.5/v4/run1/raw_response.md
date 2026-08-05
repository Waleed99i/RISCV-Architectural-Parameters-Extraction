parameters:
  - name: CacheBlockSize
    long_name: Cache Block Size
    description: The size of a cache block in bytes. This value is implementation-specific and represents the fundamental unit of data transfer and storage in the cache system.
    type: integer
    constraints:
      implementation-specific: true
      power-of-two: true
      uniform: true
      minimum: 8
      maximum: 4096
      note: The cache block size must be a power-of-two or a Naturally Aligned Power-of-Two (NAPOT) value. For the initial set of CMO extensions, the size is required to be uniform across the entire system.
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: implementation-specific
    defined_by: RISC-V Cache Management Operations (CMO) Extension
    isa_visible: true
    confidence: high

  - name: CacheCapacity
    long_name: Cache Capacity
    description: The total storage capacity of a cache in bytes. This parameter is implementation-specific and determines the maximum amount of data that can be stored in the cache.
    type: integer
    constraints:
      implementation-specific: true
      minimum: 128
      maximum: 16777216
      note: The cache capacity depends on the implementation and cache hierarchy.
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: implementation-specific
    defined_by: RISC-V Cache Management Operations (CMO) Extension
    isa_visible: true
    confidence: high

rejected: []