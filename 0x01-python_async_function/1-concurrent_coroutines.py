#!/usr/bin/env python3
""" Let's execute multiple coroutines
    at the same time with async """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax.py').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays: List[float] = []
    sorted_delays: List[float] = []
    for i in range(0, n):
        delays.append(wait_random(n))
    for delay in asyncio.as_completed(delays):
        current_delay = await delay
        sorted_delays.append(current_delay)
    return sorted_delays
