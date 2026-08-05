parameters:
  - name: CACHE_BLOCK_SIZE
    type: integer
    description: "Size of a cache block; implementation-specific. Cache blocks represent a contiguous, naturally aligned power-of-two (NAPOT) range of memory locations. Shall be uniform throughout the system in the initial set of CMO extensions."
    constraints:
      - power_of_two
      - uniform_across_system
  - name: CACHE_CAPACITY
    type: integer
    description: "Capacity of a cache; implementation-specific."
    constraints: []
  - name: CACHE_ORGANIZATION
    type: string
    description: "Organization of a cache; implementation-specific."
    constraints: []
  - name: CACHE_DISCOVERY_MECHANISM
    type: boolean
    description: "The execution environment provides software a means to discover information about the caches and cache blocks in a system."
    constraints: []