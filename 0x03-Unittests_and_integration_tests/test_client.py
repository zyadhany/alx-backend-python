#!/usr/bin/env python3
"""
Unittests for client module
"""

import unittest
from typing import Dict, Tuple, Union
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
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
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            org = {"repos_url": "http://google.com"}
            mock_org.return_value = org
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, org["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """ test_public_repos """
        payload = [{"name": "google"}, {"name": "abc"}]
        mock_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url') as mock_pub:
            mock_pub.return_value = "hello"
            client = GithubOrgClient("google")
            res = client.public_repos()
            self.assertEqual(res, ["google", "abc"])
            mock_json.called_with_once()
            mock_pub.called_with_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, license_key: str, expected: bool):
        """ test_has_license """
        client = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(client, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ TestIntegrationGithubOrgClient """
    @classmethod
    def setUpClass(cls):
        """ setUpClass """
        config = {"return_value.json.side_effect": [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload
        ]}

        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repo(self):
        """ test_public_repo """
        test_class = GithubOrgClient('Google')

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """ test_public_repos_with_license """
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """ tearDownClass """
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
