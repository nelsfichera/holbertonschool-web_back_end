#!/usr/bin/env python3
""" Asynchronous coroutine which takes an integer argument
    and waits for a random delay between 0 and max delay [default 10]
    then returns """
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """ takes in int and float which equals delay before return """
    time = uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
