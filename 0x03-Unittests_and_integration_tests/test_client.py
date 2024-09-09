#!/usr/bin/env python3
"""
    Module implementing test classes for GithubOrgClient

"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from utils import get_json
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient"""
    @parameterized.expand([
        ("google", {"login": "google", "id": 1, "repos_url":
                             "https://api.github.com/orgs/google/repos"}),
        ("abc", {"login": "abc", "id": 2, "repos_url":
                          "https://api.github.com/orgs/abc/repos"}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected_json, mock_get_json):
        """Test GithubOrgClient"""
        mock_get_json.return_value = expected_json

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with
        (GithubOrgClient.ORG_URL.format(org=org_name))
        self.assertEqual(result, expected_json)

    def test_public_repos_url(self):
        """Tests GithubOrgClient._public_repos_url method"""
        expected_payload = {"login": "google", "repos_url":
                            "https://api.github.com/orgs/google/repos"}
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = expected_payload
            client = GithubOrgClient("google")
            result = client._public_repos_url

            self.assertEqual(result, expected_payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Tests public_repos method"""
        test_payload = [
                {"name": "repo1", "license": {"key": "mit"}},
                {"name": "repo2", "license": {"key": "apache-2.0"}},
                {"name": "repo3", "license": {"key": "gpl-3.0"}}
                ]
        mock_get_json.return_value = test_payload
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value =\
                    "https://api.github.com/orgs/test/repos"
            client = GithubOrgClient("test")
            result = client.public_repos()

            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected_repos)

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with
            ("https://api.github.com/orgs/test/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),
        ({"license": None}, "my_license", False),
        ({"license": {"key": None}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Tests the GithubOrgClient.has_license method"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
