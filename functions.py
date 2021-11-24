"""
Python string manipulation exercises 
from https://igotanoffer.com/blogs/tech/string-interview-questions
"""

def longest_substring_no_repetitions(s):
    """
    Given a string s, find the length of the 
    longest substring without repeating characters.
    """
    max = 0
    longest = []
    unique_substrings = []
    for c in s:
        if c not in unique_substrings:
            unique_substrings.append(c)
            if len(unique_substrings) > max:
                max = len(unique_substrings)
                longest = unique_substrings
        else:
            unique_substrings = []
    return max, "".join(longest)


def longest_palindromic_substring(s):
    """
    Given a string s, return the longest 
    palindromic substring in s.
    """
    length = 0
    longest_palindromic = s[:1]
    for i, c in enumerate(s):
        substring = c
        for j in range(len(s) - i - 1):
            # add right
            substring = substring + s[i + j + 1]
            if substring == substring[::-1]:
                if len(substring) > length:
                    length = len(substring)
                    longest_palindromic = substring
            # add left
            if i - j - 1 >= 0:
                substring = s[i - j - 1] + substring
                if substring == substring[::-1]:
                    length = len(substring)
                    longest_palindromic = substring

    return longest_palindromic

def string_to_integer(s):
    """
    Implement atoi which removes non numeric characters from 
    a string and converts to integer
    """
    clean_string = ""
    sign = 1
    for i, c in enumerate(s):
        if c.isnumeric():
            clean_string += c
        else:
            if c == "-" and s[i + 1].isnumeric():
                sign = -1
    return int(clean_string) * sign

