#!/usr/bin/env python3
""" Tasks """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ The code is nearly identical to wait_n except task_wait_random is being
    called. """
    delays: List[float] = []
    sorted_delays: List[float] = []
    for i in range(n):
        delays.append(task_wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        sorted_delays.append(earliest_result)
    return sorted_delays
