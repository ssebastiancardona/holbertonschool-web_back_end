#!/usr/bin/env python3
"""4 tasks"""

from typing import List
task_wait_ran = __import__('3-tasks').task_wait_ran


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """function
    tasks4"""
    engen_ls = []
    esp_ls = []
    for i in range(n):
        delayed_task = task_wait_ran(max_delay)
        delayed_task.add_done_callback(lambda x: esp_ls.append(x.result()))
        engen_ls.append(delayed_task)

    for spawn in engen_ls:
        await spawn

    return esp_ls