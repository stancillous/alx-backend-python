#!/usr/bin/env python3
from typing import TypeVar, Any, Union, Mapping
"""
Given the parameters and the return values,
add type annotations to the function
"""

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> \
        Union[Any, T]:
    """adding annotations of the function"""
    if key in dct:
        return dct[key]
    else:
        return default
