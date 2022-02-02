#!/usr/bin/env python3
""" Write regular syntax async function as before calling task_wait_random """

import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn task_wait_random n times with the specified max_delay.
    """
    queue, array = [], []

    for _ in range(n):
        queue.append(task_wait_random(max_delay))

    for qu in asyncio.as_completed(queue):
        result = await qu
        array.append(result)

    return array
