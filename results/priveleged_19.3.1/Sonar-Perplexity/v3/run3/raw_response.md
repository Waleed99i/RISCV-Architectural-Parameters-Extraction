parameters:
  - name: cache_block_size
    long_name: cache block size
    description: The implementation selects the size of each cache block. The execution environment provides software with a way to discover cache block information, and the size must be uniform throughout the system in the initial CMO extensions.
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
    description: The overall cache capacity is chosen by the implementation and cache information is discoverable through the execution environment.
    type: implementation-specific parameter
    constraints:
      - implementation-specific
      - software discoverable
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: "The capacity and organization of a cache"
    defined_by: "Snippet1"
    isa_visible: true
    confidence: medium

  - name: cache_organization
    long_name: cache organization
    description: The cache organization is implementation-dependent, and software can obtain cache-related information from the execution environment.
    type: implementation-specific parameter
    constraints:
      - implementation-specific
      - software discoverable
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: "The capacity and organization of a cache"
    defined_by: "Snippet1"
    isa_visible: true
    confidence: medium

rejected: []