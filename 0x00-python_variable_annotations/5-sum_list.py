#!/usr/bin/env python3
"""5 sumList"""

from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """function"""
    return reduce(lambda a, b: a+b, input_list)
