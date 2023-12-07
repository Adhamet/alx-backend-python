#!/usr/bin/env python3
"""
    Callable, function inside a function,
    function that returns a function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Args:
            multiplier: factor

        Return:
            multiplication in float
    """

    def x(f: float) -> float:
        """Get the second argument"""
        return float(f * multiplier)

    return x
