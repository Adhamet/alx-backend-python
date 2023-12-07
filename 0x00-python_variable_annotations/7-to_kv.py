#!/usr/bin/env python3
"""
    Mixed Tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Args:
            k: String
            v: Union: Can be int or float

        Return:
            Tuple with string and int or float
    """

    result: Tuple(str, Union[int, float])
    result = (k, v**2)

    return result
