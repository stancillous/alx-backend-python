#!/usr/bin/env python3
"""
write an async routine, that will spawn the wait_random func n times
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
    write an async routine, that will spawn
    the wait_random func n times
    """
    lst = []
    for i in range(n):
        res = await wait_random(max_delay)
        lst.append(res)
    return lst
