"""Tests for password strength scoring logic."""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from strength import calculate_entropy, check_strength, has_common_pattern, has_repeated_characters


class TestStrength(unittest.TestCase):
    def test_weak_password_short_and_simple(self):
        self.assertEqual(check_strength("abc123"), "Weak")

    def test_strong_password_long_and_varied(self):
        self.assertEqual(check_strength("Xk9#mQ2$vLp7!zRt"), "Strong")

    def test_empty_password_is_weak(self):
        self.assertEqual(check_strength(""), "Weak")

    def test_common_pattern_detected(self):
        self.assertTrue(has_common_pattern("MyPassword123"))
        self.assertFalse(has_common_pattern("Xk9#mQ2$vLp7"))

    def test_repeated_characters_detected(self):
        self.assertTrue(has_repeated_characters("aaaa1234"))
        self.assertFalse(has_repeated_characters("abcd1234"))

    def test_entropy_increases_with_length(self):
        short_entropy = calculate_entropy("Ab1#")
        long_entropy = calculate_entropy("Ab1#Ab1#Ab1#")
        self.assertGreater(long_entropy, short_entropy)


if __name__ == "__main__":
    unittest.main()
