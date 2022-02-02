#!/usr/bin/env python3
""" Basic annotations """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Duck typing """
    if lst:
        return lst[0]
    else:
        return None