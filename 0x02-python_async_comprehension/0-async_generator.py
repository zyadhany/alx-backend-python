#!/usr/bin/env python3
"""
    task 0
"""

import asyncio
import random


async def async_generator():
    """
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
