#!/usr/bin/env python3
"""
    task 0
"""

import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    """
    return [i async for i in async_generator()]
