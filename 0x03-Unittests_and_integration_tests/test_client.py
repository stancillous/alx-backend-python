#!/usr/bin/env python3
"""
implement a class that will be used for
writing unittests for our funcs in the client module
"""
from unittest import TestCase
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from typing import Dict
GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubClient(TestCase):
    """class to test our funcs in the client module"""

    @parameterized.expand([
         ("google", {"user": "stancillous"}),
         ("abc", {"user": "stancillous"})
    ])
    @patch("client.get_json")
    def test_org(self, url: str, expected_output: Dict) -> None:
        """func to test the function works as expected"""
        mocked_response = MagicMock()
        mocked_response.json.return_value = expected_output
        gh_client = GithubOrgClient(url)
        self.assertEqual(gh_client.org(), expected_output)
        mocked_response.assert_called_once_with(
            f"https://api.github.com.orgs/{url}"
        )
        # mocked_function.return_value = MagicMock(
        #     return_value=expected_output)
        # goclient = GithubOrgClient(origin)
        # self.assertEqual(goclient.org(), expected_output)
        # mocked_function.assert_called_once_with(
        #     "https://api.github.com/orgs/{}".format(origin)
        # )
