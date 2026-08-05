parameters:
  - name: cache_block_size
    long_name: cache block size
    description: The size of a cache block is implementation-specific and must be discoverable by software; in the initial set of CMO extensions it must be uniform throughout the system.
    type: implementation-specific parameter
    constraints:
      - implementation-specific
      - uniform throughout the system in the initial set of CMO extensions
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system. In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    trigger: "the size of a cache block are both implementation-specific"
    defined_by: "Snippet1"
    isa_visible: true
    confidence: high

  - name: cache_capacity
    long_name: cache capacity
    description: The capacity of a cache is implementation-specific and software is provided a way to discover cache information.
    type: implementation-specific parameter
    constraints:
      - implementation-specific
      - discoverable by software via the execution environment
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: "The capacity and organization of a cache"
    defined_by: "Snippet1"
    isa_visible: true
    confidence: medium

  - name: cache_organization
    long_name: cache organization
    description: The organization of a cache is implementation-specific and software can discover cache information through the execution environment.
    type: implementation-specific parameter
    constraints:
      - implementation-specific
      - discoverable by software via the execution environment
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: "The capacity and organization of a cache"
    defined_by: "Snippet1"
    isa_visible: true
    confidence: medium

rejected: []