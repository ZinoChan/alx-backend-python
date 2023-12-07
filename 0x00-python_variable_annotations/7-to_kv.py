#!/usr/bin/env python3
"""Takes string or int/float and return a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes string or int/float and return a tuple"""
    sqr: float = v ** 2
    return (k, sqr)
