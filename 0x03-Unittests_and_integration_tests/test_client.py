#!/usr/bin/env python3
"""
    task 0
"""

import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
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

    def test_public_repos_url(self):
        """ test_public_repos_url """
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            org = {"repos_url": "http://google.com"}
            mock_org.return_value = org
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, org["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """ test_public_repos """
        payload = [{"name": "google"}, {"name": "abc"}]
        mock_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url') as mock_public_repos_url:
            mock_public_repos_url.return_value = "hello"
            client = GithubOrgClient("google")
            res = client.public_repos()
            self.assertEqual(res, ["google", "abc"])
            mock_json.called_with_once()
            mock_public_repos_url.called_with_once()


if __name__ == '__main__':
    unittest.main()
