parameters:


name: cache_capacity
long_name: Cache Capacity
description: The total storage size of the cache.
type: integer
constraints: implementation-specific, discoverable
excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
trigger: implementation-specific
defined_by: execution_environment
isa_visible: true
confidence: high


name: cache_organization
long_name: Cache Organization
description: The structural layout of the cache (e.g., associativity, number of sets).
type: string
constraints: implementation-specific, discoverable
excerpt: "The capacity and organization of a cache and the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system."
trigger: implementation-specific
defined_by: execution_environment
isa_visible: true
confidence: high


name: cache_block_size
long_name: Cache Block Size
description: The size of each cache block, representing a contiguous, naturally aligned power-of-two or NAPOT range of memory locations.
type: integer
constraints: implementation-specific, discoverable, power-of-two or NAPOT, naturally aligned, uniform throughout the system (for initial CMO extensions)
excerpt: "the size of a cache block are both implementation-specific, and the execution environment provides software a means to discover information about the caches and cache blocks in a system. In the initial set of CMO extensions, the size of a cache block shall be uniform throughout the system."
trigger: implementation-specific
defined_by: execution_environment, CMO_extensions
isa_visible: true
confidence: high

rejected:


candidate: cache_block_alignment
category: Architectural Constraint
reason: CONSTRAINT_NOT_PARAMETER
excerpt: "each of which represents a contiguous, naturally aligned power-of-two (or NAPOT) range of memory locations."
explanation: The alignment is a constraint on cache blocks, not a configurable parameter.


candidate: cache_block_identification
category: Microarchitectural Detail
reason: NOT_ISA_VISIBLE
excerpt: "A cache block is identified by any of the physical addresses corresponding to the underlying memory locations."
explanation: The identification mechanism is a microarchitectural detail and not visible to software via the ISA.