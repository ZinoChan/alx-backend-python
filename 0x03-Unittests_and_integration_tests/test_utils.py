import unittest
from parameterized import parameterized
from utils import utils


class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result) -> None:
        """TEst access nested map"""
        self.assertEqual(utils.access_nested_map(
            nested_map, path), expected_result)
