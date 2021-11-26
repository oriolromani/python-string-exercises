"""
Python string manipulation exercises 
from https://igotanoffer.com/blogs/tech/string-interview-questions
"""
import itertools

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

def reduced_string(k, s):
    """
    Given a string s and an integer k, the task is to reduce the 
    string by applying the following operation:
    Choose a group of k consecutive identical characters and remove them.
    The operation can be performed any number of times until 
    it is no longer possible.
    """
    indexes_to_remove = set()
    do_not_check = []
    for i in range(len(s)- k):
        if i in do_not_check:
            continue
        if len(set(s[i:i+k])) == 1:
            indexes_to_remove.update(range(i, i+k))
            do_not_check = range(i, i+k+1)
    if not indexes_to_remove:
        return s
    else:
        new_string = ""
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                new_string += c
        return reduced_string(k, new_string)

def find_longest_word(s, d):
    """
    Given a string and a string dictionary, 
    find the longest string in the dictionary 
    that can be formed by deleting some characters 
    of the given string. 
    If there are more than one possible results, 
    return the longest word with the smallest lexicographical order. 
    If there is no possible result, return the empty string.
    TODO: optimise performance
    """
    max_len = 0
    results = []
    for l in range(1, len(s)):
        for subset in itertools.combinations(s, l):
            word = "".join(subset)
            if word in d and len(word) > max_len:
                results.append(word)
                max_len = len(word)
    max_results = [result for result in results if len(result) == max_len]
    max_results.sort()
    return max_results[0]