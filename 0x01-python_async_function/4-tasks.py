#!/usr/bin/env python3
"""
    Task 4
"""

from typing import List
import asyncio
import random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    """
    sl = []
    dl = []
    for i in range(n):
        dy = task_wait_random(max_delay)
        dy.add_done_callback(lambda x: dl.append(x.result()))
        sl.append(dy)

    for spawn in sl:
        await spawn

    return dl
