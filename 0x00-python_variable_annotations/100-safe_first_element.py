#!/usr/bin/env python3

"""
    task 100
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    """

    if lst:
        return lst[0]
    else:
        return None
