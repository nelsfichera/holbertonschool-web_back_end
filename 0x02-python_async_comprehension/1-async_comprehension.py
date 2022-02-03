#!/usr/bin/env python3
"""Coroutine which loops 10 times,
        asynchronously wait one second,
        then yield a random number between 0 and 10
        using the random module. """
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ take no arguments, comprehense over async_generator
            and return 10 random numbers """
    random_num_list = [i async for i in async_generator()]
    return random_num_list
