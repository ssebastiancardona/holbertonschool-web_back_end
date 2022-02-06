#!/usr/bin/env python3
"""3 tasks"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Devuelve una tarea
    Argumentos:
        max_delay (int): número máximo de retraso
    Devoluciones:
        asyncio.Task: tarea a devolver
    """
    return asyncio.create_task(wait_random(max_delay))
