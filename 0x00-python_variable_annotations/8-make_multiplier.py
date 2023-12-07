#!/usr/bin/env python3
"""Return multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def muliply(n: float) -> float:
        return multiplier * n
    return muliply
