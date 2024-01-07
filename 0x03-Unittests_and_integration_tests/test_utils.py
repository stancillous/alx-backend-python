#!/usr/bin/env python3
"""
implement a class that will be used for
writing unittests for our code
"""
import requests
from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized

access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """method to test that appropriate exception is raised"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """class to test our get json func returns the expected response"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """test our get json func returns correct result"""
        mock_response = Mock()
        mock_response.json.return_value = payload

        with patch("requests.get", return_value=mock_response) as mock_method:
            result = get_json(url)
            self.assertEqual(result, payload)

        mock_method.assert_called_once_with(url)


class TestMemoize(TestCase):
    """class with methods to test our memoize func"""

    def test_memoize(self):
        """
        method to test that our memoize func
        returns expected result
        """

        class TestClass:
            """class TestClass
            """

            def a_method(self):
                """ method a_method
                """
                return 42

            @memoize
            def a_property(self):
                """ method a_property
                """
                return self.a_method()

        test_instance = TestClass()

        with patch.object(test_instance, 'a_method') as mock_method:
            mock_method.return_value = 42

            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # print("\n\n\tres1 is ", result1)
            # print("\n\n\tres2 is ", result2)
            self.assertEqual(result2, 42)
            self.assertEqual(result1, 42)
            mock_method.assert_called_once()
