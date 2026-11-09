"""Tests for input validation logic."""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from validator import (
    ValidationError,
    parse_length_input,
    parse_yes_no,
    validate_character_options,
    validate_length,
)


class TestValidator(unittest.TestCase):
    def test_validate_length_within_bounds(self):
        self.assertEqual(validate_length(10, 6, 64), 10)

    def test_validate_length_below_minimum(self):
        with self.assertRaises(ValidationError):
            validate_length(4, 6, 64)

    def test_validate_length_above_maximum(self):
        with self.assertRaises(ValidationError):
            validate_length(100, 6, 64)

    def test_validate_length_rejects_non_integer(self):
        with self.assertRaises(ValidationError):
            validate_length("12", 6, 64)

    def test_validate_character_options_requires_one(self):
        with self.assertRaises(ValidationError):
            validate_character_options(False, False, False, False)

    def test_parse_length_input_valid(self):
        self.assertEqual(parse_length_input(" 16 "), 16)

    def test_parse_length_input_invalid(self):
        with self.assertRaises(ValidationError):
            parse_length_input("abc")

    def test_parse_yes_no_variants(self):
        self.assertTrue(parse_yes_no("y"))
        self.assertFalse(parse_yes_no("n"))
        self.assertTrue(parse_yes_no("", default=True))

    def test_parse_yes_no_invalid(self):
        with self.assertRaises(ValidationError):
            parse_yes_no("maybe")


if __name__ == "__main__":
    unittest.main()
