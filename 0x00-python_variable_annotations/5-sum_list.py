#!/usr/bin/env python3
"""Sum up floats"""
from functools import reduce


def sum_list(input_list: list[float]) -> float:
    """sum of floats"""
    return reduce(lambda x, y: x + y, input_list)
