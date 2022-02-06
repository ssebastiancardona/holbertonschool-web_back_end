#!/usr/bin/env python3
"""2 measure
ensure advanced"""
import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """medir el tiempo de ejecución
    retorna:
        float: tiempo
    """
    inicio = time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    fin = time()
    return fin - inicio
