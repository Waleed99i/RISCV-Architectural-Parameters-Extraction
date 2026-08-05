parameters:
  - name: cache_block_size
    long_name: cache block size
    description: The cache block size is implementation-specific. Software can discover cache block information, and the size is required to be uniform throughout the system for the initial CMO extensions.
    type: implementation-specific parameter
    constraints:
      - implementation-specific
      - uniform throughout the system for the initial CMO extensions
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system. In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
    trigger: "implementation-specific"
    defined_by: "Snippet1"
    isa_visible: true
    confidence: high

  - name: cache_capacity
    long_name: cache capacity
    description: The capacity of a cache is chosen by the implementation, and cache information is discoverable by software.
    type: implementation-specific parameter
    constraints:
      - implementation-specific
      - discoverable through the execution environment
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: "implementation-specific"
    defined_by: "Snippet1"
    isa_visible: true
    confidence: medium

  - name: cache_organization
    long_name: cache organization
    description: The organization of a cache is implementation-specific and information about it can be obtained through the execution environment.
    type: implementation-specific parameter
    constraints:
      - implementation-specific
      - discoverable through the execution environment
    excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
    trigger: "implementation-specific"
    defined_by: "Snippet1"
    isa_visible: true
    confidence: medium

rejected: []