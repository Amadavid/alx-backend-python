#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Complex types - functions
    """
    def inner_multiplier(f: float) -> float:
        """
        Complex types - functions
        """
        return f * multiplier
    return inner_multiplier
