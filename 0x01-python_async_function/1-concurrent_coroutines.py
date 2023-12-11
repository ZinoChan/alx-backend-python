#!/usr/bin/env python3
"""Execuute multiple coroutines"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execuute multiple coroutines"""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    futur_delays: List[float] = asyncio.as_completed(coroutines)
    return [await delay for delay in futur_delays]
