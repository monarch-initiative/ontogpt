"""Tests for parse_utils.sanitize_text."""

import unittest

from ontogpt.utils.parse_utils import sanitize_text


class TestSanitizeText(unittest.TestCase):
    def test_none_and_empty(self):
        self.assertEqual(sanitize_text(None), "")
        self.assertEqual(sanitize_text(""), "")

    def test_no_changes(self):
        s = "Hello World"
        self.assertEqual(sanitize_text(s), s)

    def test_preserve_allowed_whitespace(self):
        s = "Line1\nLine2\tTabbed\rCarriage"
        self.assertEqual(sanitize_text(s), s)

    def test_remove_ascii_control_chars(self):
        s = "A\x00B\x04C\x1FD"  # NUL, EOT, US
        self.assertEqual(sanitize_text(s), "ABCD")

    def test_remove_del_and_c1(self):
        s = "X\x7FY"  # DEL should be removed
        self.assertEqual(sanitize_text(s), "XY")

    def test_remove_format_chars(self):
        # ZERO WIDTH SPACE (U+200B) is Cf and should be removed
        s = "A\u200B B"
        # After removal we expect the characters on either side
        # to be concatenated with existing space preserved
        self.assertEqual(sanitize_text(s), "A B")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
