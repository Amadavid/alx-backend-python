#!/usr/bin/env python3
"""
write an async routine called wait_n that takes in 2
int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.
"""

import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    method to wait for return value
    """
    wait_list: list = []
    for n in range(n):
        wait_list.append(await wait_random(max_delay))
    wait_list.sort()
    return wait_list
