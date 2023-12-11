#!/usr/bin/env python3
"""async coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for random time"""
    await asyncio.sleep(random.random() * max_delay)
    return max_delay
