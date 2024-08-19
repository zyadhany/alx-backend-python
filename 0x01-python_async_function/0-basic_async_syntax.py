#!/usr/bin/env python3
"""
    task 0
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    """
    act: float = random.uniform(0, max_delay)
    await asyncio.sleep(act)
    return act
