parameters:
  - name: CACHE_BLOCK_SIZE
    type: integer
    description: "Size of a cache block; implementation-specific."
    constraints:
      - power_of_two
      - uniform_across_system
  - name: CACHE_CAPACITY
    type: integer
    description: "Capacity of a cache; implementation-specific."
    constraints: []
  - name: CACHE_ORGANIZATION
    type: enum
    description: "Organization of a cache; implementation-specific."
    constraints: []