"""Tests for parse_utils.sanitize_text and parse_utils.is_null_like_value."""

import unittest

from ontogpt.utils.parse_utils import is_null_like_value, sanitize_text


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


class TestIsNullLikeValue(unittest.TestCase):
    def test_none_and_empty(self):
        self.assertTrue(is_null_like_value(None))
        self.assertTrue(is_null_like_value(""))
        self.assertTrue(is_null_like_value("   "))

    def test_placeholder_tokens(self):
        for token in [
            "none",
            "None",
            "N/A",
            "n/a",
            "NA",
            "null",
            "nil",
            "NaN",
            "unknown",
            "unspecified",
            "not specified",
            "Not Applicable",
            "none provided",
            "no value",
        ]:
            self.assertTrue(is_null_like_value(token), f"expected {token!r} to be null-like")

    def test_template_echo_is_null_like(self):
        # The model sometimes echoes the prompt placeholder back verbatim.
        self.assertTrue(is_null_like_value("<the food item>"))
        self.assertTrue(is_null_like_value("<no url provided>"))

    def test_wrapped_placeholders_are_null_like(self):
        # Models wrap placeholders in brackets/quotes/emphasis or add trailing
        # punctuation; these should still be treated as "no value".
        for token in ["(none)", "[N/A]", "*none*", "none.", "'none'", "(None)", "{n/a}"]:
            self.assertTrue(is_null_like_value(token), f"expected {token!r} to be null-like")

    def test_real_values_are_not_null_like(self):
        for value in [
            "turkey",
            "non-fat milk",  # contains "n/a" as a substring, but is a real value
            "cooking spray",
            "2 pounds",
            "0",
            "none of the above sauces",  # starts with "none" but is real text
        ]:
            self.assertFalse(is_null_like_value(value), f"expected {value!r} to be a real value")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
