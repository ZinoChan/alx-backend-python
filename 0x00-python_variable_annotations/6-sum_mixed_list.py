#!/usr/bin/env python3
"""Sum_mixed_list"""

from functools import reduce
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum of mixed"""
    return reduce(lambda x, y: x + y, mxd_lst)
