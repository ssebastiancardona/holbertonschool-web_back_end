#!/usr/bin/env python3
"""1 async comprehension
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """crear una lista con 10 números al azar
    Devoluciones:
        List[float]: una lista con el resultado del método generador asíncrono
    """
    return [n async for n in async_generator()]
