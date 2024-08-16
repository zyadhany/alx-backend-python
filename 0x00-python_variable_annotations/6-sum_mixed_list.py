#!/usr/bin/env python3

"""
    task 6
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    """

    sum = 0.0

    for num in mxd_lst:
        sum += num

    return sum
