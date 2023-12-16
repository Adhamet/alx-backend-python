#!/usr/bin/env python3
""" Let's execute multiple coroutines
    at the same time with async """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort()
    because of concurrency. """
    delays: List[float] = []
    sorted_delays: List[float] = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        sorted_delays.append(earliest_result)
    return sorted_delays
