#!/usr/bin/env python3
from typing import List, Union
"""
type-annotated function sum_mixed_list which takes a
list mxd_lst of integers and floats and returns their sum as a float
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of integers and floats in the mixed list as a float.
    """
    return float(sum(mxd_lst))
