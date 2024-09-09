#!/usr/bin/env python3
"""
    task 0
"""

import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, expected: Dict, mock_get_json: Mock):
        """ test_org """
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.called_with_once(client.ORG_URL.format(org=org_name))


if __name__ == '__main__':
    unittest.main()
