#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from unittest.mock import Mock, patch
from utils import (
    access_nested_map,
    get_json,
    memoize
)


class TestAccessNestedMap(unittest.TestCase):
    """Tests the access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected_results: Union[Dict, int],
    ) -> None:
        """Tests access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected_results)

    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected_exception: Exception,
    ) -> None:
        """Tests access_nested_map"""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test Json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):

    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch('utils.TestMemoize.TestClass.a_method')
    def test_memoize(self, mock_a_method):
        """Tests memoize output."""
        test_instance = self.TestClass()

        result_1 = test_instance.a_property()
        mock_a_method.assert_called_once()

        mock_a_method.reset_mock()

        result_2 = test_instance.a_property()
        mock_a_method.assert_not_called()

        self.assertEqual(result_1, result_2)
