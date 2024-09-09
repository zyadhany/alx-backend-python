#!/usr/bin/env python3
"""
    task 0
"""

import asyncio
import random
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    """
    cur = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - cur
