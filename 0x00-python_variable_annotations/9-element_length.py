#!/usr/bin/env python3

"""
    task 9
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    """
    return [(i, len(i)) for i in lst]
