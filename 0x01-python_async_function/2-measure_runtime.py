#!/usr/bin/env python3
"""
 writing a function that measures the total execution time for
 wait_n(n, max_delay), and returns total_time / n
"""
import time
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n, max_delay):
    """
    function that measures the total execution time for wait_n(n, max_delay)
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - start_time
    return float(elapsed_time / n)
