#!/usr/bin/env python3
"""2 measure runtime"""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """funcion
    return seblapsed"""
    seb = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    seblapsed = time.perf_counter() - seb
    return seblapsed/n
