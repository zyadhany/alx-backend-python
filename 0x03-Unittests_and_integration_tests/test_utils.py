#!/usr/bin/env python3
"""
    task 0
"""

import unittest
from utils import access_nested_map, get_json, memoize
from typing import Dict, Tuple, Union
from parameterized import parameterized
from unittest.mock import patch, Mock


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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, dic: Dict, path: Tuple[str],
                                         exp: Exception) -> None:
        """test_access_nested_map_exception"""
        with self.assertRaises(exp):
            access_nested_map(dic, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url: str, exp: Dict) -> None:
        """test_get_json"""
        att = {'json.return_value': exp}
        with patch('requests.get', return_value=Mock(**att)) as mock_get:
            self.assertEqual(get_json(url), exp)
            mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """TestMemoize class"""

    def test_memoize(self) -> None:
        """ test_memoize """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            tc = TestClass()
            self.assertEqual(tc.a_property, 42)
            self.assertEqual(tc.a_property, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
