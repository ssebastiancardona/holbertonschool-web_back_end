#!/usr/bin/env python3
"""1 concurrent
coroutines"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function
    return"""
    d = []
    for _ in range(n):
        d.append(await wait_random(max_delay))
    return [i for i in sorted(d)]
