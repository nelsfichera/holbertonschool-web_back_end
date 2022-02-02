#!/usr/bin/env python3
''' Async routine which takes in two arguments n & delay
    wait_random will wait n times of max_delay'''


import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''spawn wait_random n times and returns list of delays
        in ascending order without using sort()'''
    queue, array = [], []

    for _ in range(n):
        queue.append(wait_random(max_delay))

    for qu in asyncio.as_completed(queue):
        result = await qu
        array.append(result)

    return array
