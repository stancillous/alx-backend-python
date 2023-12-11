#!/usr/bin/env python3
"""
Write an asynchronous coroutine named wait_random
that waits for a random delay between 0 and max_delay
seconds and eventually returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """async func that takes an arg, waits for  a random delay,
    and then returns it"""
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
