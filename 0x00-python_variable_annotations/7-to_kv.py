#!/usr/bin/env python3
from typing import Union, Tuple
"""
type-annotated function to_kv that takes a string k and an int OR float v as
arguments and returns a tuple.
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ function that takes a str and int or float as arguments
    and returns a tuple"""
    square: float = v * v
    return (k, square)
