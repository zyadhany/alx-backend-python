#!/usr/bin/env python3
"""
    task 0
"""

import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    def test_access_nested_map(self):
        """test_access_nested_map"""
        self.assertEqual(access_nested_map({"a": 1}, ('a',)), 1)
        self.assertEqual(access_nested_map({"a": {"b": 2}}, ('a',)), {"b": 2})
        self.assertEqual(access_nested_map({"a": {"b": 2}}, ('a', 'b')), 2)


if __name__ == '__main__':
    unittest.main()
