#!/usr/bin/env python3
"""
Takes 2
"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    """
    sl = []
    dl = []
    for i in range(n):
        delayed_task = asyncio.create_task(wait_random(max_delay))
        delayed_task.add_done_callback(lambda x: dl.append(x.result()))
        sl.append(delayed_task)

    for spawn in sl:
        await spawn

    return dl
