#!/usr/bin/env python3
""" Basic annotations """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ returns sum as a float """
    return sum(mxd_lst)