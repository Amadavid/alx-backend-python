#!/usr/bin/env python3
"""
Let's duck type an iterable object
"""
from typing import List, Tuple, Union, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Let's duck type an iterable object
    """
    return[(i, len(i)) for i in lst]
