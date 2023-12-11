#!/usr/bin/env python3
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
"""
writing a function that takes an integer
max_delay and returns a asyncio.Task
"""


def task_wait_random(max_delay):
    """function takes an integer max_delay and
        returns a asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
