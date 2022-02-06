#!/usr/bin/env python3
"""0 basic async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """funcion
    random segundos"""
    segundos = random.uniform(0, max_delay)
    await asyncio.sleep(segundos)
    return segundos
