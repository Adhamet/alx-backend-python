#!/usr/bin/env python3
""" Async Comprenhesion """
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Generate numbers with async comprenhension. """
    return ([i async for i in async_generator()])
