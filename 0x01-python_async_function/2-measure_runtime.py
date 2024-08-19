#!/usr/bin/env python3
"""
    Task 3
"""

import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    """

    et: float

    st = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    et = time.perf_counter() - st
    return et / n