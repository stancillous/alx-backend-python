#!/usr/bin/env python3
from typing import Callable
""""
type-annotated function make_multiplier that takes
a float multiplier as argument and returns a function
that multiplies a float by multiplier
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    func that takes a float and returns a function
    """
    def multiplier_func(num: float) -> float:
        return num * multiplier
    return multiplier_func
