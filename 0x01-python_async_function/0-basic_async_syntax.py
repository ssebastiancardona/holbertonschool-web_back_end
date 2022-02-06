#!/usr/bin/env python3
"""modulo de espera
medio loco"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """espera numero aleatorio
    Argumentos:
        max_delay (int, opcional): número máximo. El valor predeterminado es 10.
    Devoluciones:
        flotante: número flotante aleatorio
    """
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
