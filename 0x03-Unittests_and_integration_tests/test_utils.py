#!/usr/bin/env python3
"""Unit tests for utility functions in the utils module."""

import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""

    @parameterized.expand([
        ({"key_a": 1}, ("key_a",), 1),
        ({"key_a": {"key_b": 2}}, ("key_a",), {"key_b": 2}),
        ({"key_a": {"key_b": 2}}, ("key_a", "key_b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_data: Dict,
            key_path: Tuple[str],
            expected_result: Union[Dict, int],
    ) -> None:
        """Tests the access_nested_map function."""
        self.assertEqual(access_nested_map(
            nested_data, key_path), expected_result)

    @parameterized.expand([
        ({}, ("key_a",), KeyError),
        ({"key_a": 1}, ("key_a", "key_b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_data: Dict,
            key_path: Tuple[str],
            expected_exception: Exception,
    ) -> None:
        """Tests the exception handling of access_nested_map."""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_data, key_path)

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
    ) -> None:
        """Tests the get_json function."""
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            req_get.assert_called_once_with(test_url)

    def test_memoize(self) -> None:
        """Tests the memoize function."""
        class TestClass:
            """Sample class for testing memoization."""

            def a_method(self):
                """A sample method."""
                return 42

            @memoize
            def a_property(self):
                """A sample memoized property."""
                return self.a_method()

        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
        ) as memoized_method:
            test_instance = TestClass()
            self.assertEqual(test_instance.a_property(), 42)
            self.assertEqual(test_instance.a_property(), 42)
            memoized_method.assert_called_once()
