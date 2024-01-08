#!/usr/bin/env python3
"""
implement a class that will be used for
writing unittests for our funcs in the client module
"""
from unittest import TestCase
from parameterized import parameterized
from unittest.mock import patch, MagicMock, Mock, PropertyMock
from typing import Dict
GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubClient(TestCase):
    """class to test our funcs in the client module"""

    @parameterized.expand([
         ("google", {"user": "stancillous"}),
         ("abc", {"user": "stancillous"})
    ])
    @patch("client.get_json")
    def test_org(self, url: str, expected_output: Dict,
                 mocked_method: MagicMock) -> None:
        """func to test the function works as expected"""
        mocked_method.return_value = MagicMock(
            return_value=expected_output)
        gh_client = GithubOrgClient(url)
        self.assertEqual(gh_client.org(), expected_output)
        mocked_method.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(url)
        )

    def test_public_repos_url(self) -> None:
        """method to test our _public_repos_url function
        """

        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as mock_org:

            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }

            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Testing our has_license method"""
        gh_org_client = GithubOrgClient("google")
        client_has_licence = gh_org_client.has_license(repo, key)
        self.assertEqual(client_has_licence, expected)
