#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker module. """
from requests import get as GET
from typing import Callable
from functools import wraps
import redis

cache = redis.Redis()


def set_page(method: Callable) -> Callable:
    """ Sets HTML content from URL """
    @wraps(method)
    def cache_in(url):
        """ Inner decorator method. """
        cache.incr(f"count:{url}", 1)

        cached_html = cache.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        text = method(url)
        cache.setex(f"cached:{url}", 10, text)
        return text

    return cache_in


@set_page
def get_page(url: str) -> str:
    """ gets HTML content from URL and treturns it """
    r = GET(url)
    return r.text
