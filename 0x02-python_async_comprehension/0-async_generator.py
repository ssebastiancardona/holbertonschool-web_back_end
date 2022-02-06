#!/usr/bin/env python3
"""0 async generator"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """function
    async generator"""
    nf: int = 10
    for i in range(nf):
        await asyncio.sleep(1)
        yield random.uniform(0, nf)
