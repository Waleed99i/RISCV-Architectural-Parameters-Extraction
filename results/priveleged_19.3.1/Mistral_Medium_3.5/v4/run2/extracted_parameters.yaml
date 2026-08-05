parameters:

name: cache_block_alignment
long_name: Cache Block Alignment
description: The alignment requirement for cache blocks, which must be naturally aligned and either power-of-two or NAPOT.
type: string
constraints: naturally aligned, power-of-two or NAPOT
excerpt: "each of which represents a contiguous, naturally aligned power-of-two (or NAPOT) range of memory locations."
trigger: implementation-specific
defined_by: execution_environment
isa_visible: true
confidence: high
rejected:

candidate: cache_block_identification
category: Microarchitectural Detail
reason: NOT_ISA_VISIBLE
excerpt: "A cache block is identified by any of the physical addresses corresponding to the underlying memory locations."
explanation: The identification mechanism is a microarchitectural detail and not visible to software via the ISA.