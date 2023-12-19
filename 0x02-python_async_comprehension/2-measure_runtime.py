#!/usr/bin/env python3
""" Measure times """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure time and execute in parallel """
    start_time = time.perf_counter()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()

    return (end_time - start_time)
