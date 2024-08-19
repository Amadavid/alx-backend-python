#!/usr/bin/env python3
"""
altering a function into a new function
"""

from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    method to wait for return value
    """
    wait_list: list = []
    for n in range(n):
        task = task_wait_random(max_delay)
        wait_list.append(await task)
    return sorted(wait_list)
