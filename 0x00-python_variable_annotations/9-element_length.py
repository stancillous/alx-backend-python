#!/usr/bin/env python3
from typing import Iterable, Tuple, List, Sequence
"""
Annotate the below function’s parameters and
return values with the appropriate types
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """func to duck type an iterable object"""
    return [(i, len(i)) for i in lst]
