#!/usr/bin/env python3
""" take two int args & return tuple of page & page size """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ 
        returns a tuple of size two containing: a start index
        and an end index, corresponding to the range of indices
        to return in a list for those particular pagination parameters 
    """

    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)