import unittest
from functions import (
    longest_substring_no_repetitions,
    longest_palindromic_substring,
    string_to_integer
    )

class TestLongestSubstringNoRepetitions(unittest.TestCase):

    def test_longest_substring_no_repetitions(self):
        result = longest_substring_no_repetitions("abcabcbb")
        self.assertEqual((3, "abc"), result)
        result = longest_substring_no_repetitions("pwwkew")
        self.assertEqual((3, "kew"), result)
        result = longest_substring_no_repetitions("")
        self.assertEqual((0, ""), result)
        result = longest_substring_no_repetitions("bbbbbbbb")
        self.assertEqual((1, "b"), result)

class TestLongestPalindrom(unittest.TestCase):

    def test_longest_palindrom(self):
        result = longest_palindromic_substring("babad")
        self.assertEqual("aba", result)
        result = longest_palindromic_substring("cbbd")
        self.assertEqual("bb", result)
        result = longest_palindromic_substring("a")
        self.assertEqual("a", result)
        result = longest_palindromic_substring("ac")
        self.assertEqual("a", result)
        result = longest_palindromic_substring("bctnhtyhbanactycachge")
        self.assertEqual("cac", result) # it returns the last palindrom

class TestStringToInt(unittest.TestCase):

    def test_string_to_int(self):
        result = string_to_integer("42")
        self.assertEqual(42, result)
        result = string_to_integer("  -42")
        self.assertEqual(-42, result)
        result = string_to_integer("4193 with words")
        self.assertEqual(4193, result)
    

if __name__ == '__main__':
    unittest.main()
