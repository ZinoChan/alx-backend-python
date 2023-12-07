#!/usr/bin/env python3
"""Sum up floats"""
from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum of floats"""
    return float(reduce(lambda x, y: x + y, input_list))
