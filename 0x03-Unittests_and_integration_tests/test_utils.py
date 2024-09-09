#!/usr/bin/env python3
"""
    task 0
"""

import unittest
from utils import access_nested_map
from typing import Dict, Tuple, Union
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand([
        ({"a": 1}, ('a',), 1),
        ({"a": {"b": 2}}, ('a',), {"b": 2}),
        ({"a": {"b": 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, dic: Dict, path: Tuple[str],
                               exp: Union[Dict, int]) -> None:
        """test_access_nested_map"""
        self.assertEqual(access_nested_map(dic, path), exp)


if __name__ == '__main__':
    unittest.main()
