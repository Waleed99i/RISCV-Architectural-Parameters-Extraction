CACHE_BLOCK_SIZE:
  description: The size of a cache block in bytes, which must be a power of two. This is an implementation-specific parameter that determines how data is organized within the cache hierarchy.
  type: integer
  constraints:
    - minimum: 1
      maximum: 1048576
      power_of_two: true

CACHE_ORGANIZATION:
  description: The structural design of the cache, including the number of ways, the replacement policy, and the level of hierarchy (L1, L2, etc.). This is implementation-specific and affects the performance of the CPU.
  type: enum
  constraints:
    - enum_values:
        - Direct-Mapped
        - N-Way Set Associative
        - Fully Associative