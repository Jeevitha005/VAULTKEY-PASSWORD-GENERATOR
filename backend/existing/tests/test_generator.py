"""Tests for password generation logic."""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from generator import build_character_pool, generate_password
from validator import ValidationError


class TestGenerator(unittest.TestCase):
    def test_generate_password_correct_length(self):
        password = generate_password(12)
        self.assertEqual(len(password), 12)

    def test_generate_password_rejects_too_short(self):
        with self.assertRaises(ValidationError):
            generate_password(3, min_length=6)

    def test_generate_password_rejects_too_long(self):
        with self.assertRaises(ValidationError):
            generate_password(100, max_length=64)

    def test_generate_password_no_character_sets_raises(self):
        with self.assertRaises(ValidationError):
            generate_password(
                10,
                use_uppercase=False,
                use_lowercase=False,
                use_numbers=False,
                use_symbols=False,
            )

    def test_build_character_pool_excludes_ambiguous(self):
        pool = build_character_pool(True, True, True, False, exclude_ambiguous=True)
        for char in "Il1O0":
            self.assertNotIn(char, pool)

    def test_generate_password_uniqueness(self):
        passwords = {generate_password(16) for _ in range(20)}
        self.assertEqual(len(passwords), 20)


if __name__ == "__main__":
    unittest.main()
