#!/usr/bin/env python3
"""
implement a class that will be used for
writing unittests for our code
"""
from unittest import TestCase
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(TestCase):
    """
    class with methods to test our code
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """test that the method works as expected"""
        self.assertEqual(access_nested_map(nested_map, path), expected_output)
