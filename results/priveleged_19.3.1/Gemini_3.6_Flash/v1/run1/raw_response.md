parameters:

    name: CACHE_CAPACITY
    type: integer
    description: Capacity of a cache in the system.
    constraints: []

    name: CACHE_ORGANIZATION
    type: string
    description: Organization of a cache in the system.
    constraints: []

    name: CACHE_BLOCK_SIZE
    type: integer
    description: Size of a cache block representing a contiguous, naturally aligned range of memory locations.
    constraints:

        power_of_two