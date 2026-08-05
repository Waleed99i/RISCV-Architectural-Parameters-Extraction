parameters:
  - name: CACHE_CAPACITY
    description: Capacity of a cache.
    type: integer
    constraints:
      - implementation-specific

  - name: CACHE_ORGANIZATION
    description: Organization of a cache.
    type: string
    constraints:
      - implementation-specific

  - name: CACHE_BLOCK_SIZE
    description: Size of a cache block.
    type: integer
    constraints:
      - implementation-specific
      - uniform throughout the system in the initial set of CMO extensions