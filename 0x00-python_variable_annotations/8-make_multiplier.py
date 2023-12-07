#!/usr/bin/env python3
"""Return multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return multiplier function"""
    def muliply(n: float) -> float:
        """Return multiply"""
        return multiplier * n
    return muliply
