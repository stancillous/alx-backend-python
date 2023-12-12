#!/usr/bin/env python3
import asyncio
import time
"""
Import async_comprehension from the previous file and
write a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.
"""
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    func to measure runtime after calling the async_comprehension
    function four times
    """
    start_time: float = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    elapsed_time: float = time.perf_counter() - start_time
    return elapsed_time
