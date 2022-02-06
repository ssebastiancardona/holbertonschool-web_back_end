#!/usr/bin/env python3
"""7 toKv"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function"""
    return (k, v ** 2)