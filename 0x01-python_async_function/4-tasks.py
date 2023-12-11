#!/usr/bin/env python3
"""

"""
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    """
    write an async routine, that will spawn
    the wait_random func n times
    """
    lst = []
    for i in range(n):
        res = await task_wait_random(max_delay)
        lst.append(res)
    return lst
