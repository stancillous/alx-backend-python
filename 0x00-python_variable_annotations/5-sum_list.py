#!/usr/bin/env python3
from typing import List
"""
type-annotated function sum_list which takes a list input_list
of floats as argument and returns their sum as a float
"""


def sum_list(input_list: List[float]) -> float:
    """func to add all elements of a list"""
    return float(sum(input_list))
