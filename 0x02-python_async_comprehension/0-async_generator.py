#!/usr/bin/env python3
""" Async Generator """
import asyncio
import random
from typing import Generator


async def arange(numbers: int) -> Generator[int, None, None]:
    """ Function that asynchronously gets the range of numbers
    from 0 to numbers. """
    for i in range(numbers):
        yield i
        await asyncio.sleep(1)


async def async_generator() -> Generator[float, None, None]:
    """ Function that each time asynchronously waits 1 second,
    then yields a random number between 0 and 10. """
    async for i in arange(10):
        await asyncio.sleep(1)
        random_number = random.uniform(0, 10)
        yield random_number
