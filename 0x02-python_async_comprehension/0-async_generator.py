#!/usr/bin/env python3
""" Async Generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Function that each time asynchronously waits 1 second,
    then yields a random number between 0 and 10. """
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
