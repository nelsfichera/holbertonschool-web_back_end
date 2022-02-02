#!/usr/bin/env python3
""" Takes n and max delay for total execution time  """

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Meturns the float of the runtime with time module """
    start = time()

    run(wait_n(n, max_delay))

    end = time()

    return (end - start) / n
