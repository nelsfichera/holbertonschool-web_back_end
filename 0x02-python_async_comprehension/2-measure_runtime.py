#!/usr/bin/env python3
"""Coroutine which executes 
    async_comprehension four times in parallel
    using asyncio.gather. """
import asyncio
import random
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure and return total runtime """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.perf_counter()
    return end - start