# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?isFullScreen=true
#
# Sherlock considers a string to be valid if all characters of the string appear the same number of times.
# It is also valid if he can remove just  character at  index in the string,
# and the remaining characters will occur the same number of times.
# Given a string , determine if it is valid. If so, return YES, otherwise return NO.
#
# Example
# abbc
# This is a valid string because frequencies are .
#
# abc
# This is a valid string because we can remove one  and have  of each character in the remaining string.
#
# abbcc
# This string is not valid as we can only remove 1 occurrence of . That leaves character frequencies of .
#
# Function Description
#
# Complete the isValid function in the editor below.
#
# isValid has the following parameter(s):
#
# string s: a string
# Returns
#
# string: either YES or NO


# aabbbcc
# {2: 2, 3: 1}
# aabbc
# {2: 2, 1: 1}
# aaabbbcccddee
# {3: 3, 2: 2}
# aabbcccddd
# {2: 2, 3: 2}

from collections import Counter


def sherlock_valid_string(s):
    frequency = Counter(s)
    freq_range = Counter(frequency)

    if len(freq_range) == 1:
        return "YES"
    elif len(freq_range) > 2:
        return "NO"
    else:
        keys = list(freq_range.keys())
        if freq_range[keys[0]] == 1 or freq_range[keys[1]] == 1:
            if max(keys) - min(keys) == 1 \
                    or (freq_range[keys[0]] == 1 and keys[0] == 1) \
                    or (freq_range[keys[1]] == 1 and keys[1] == 1):
                return "YES"
        return "NO"


test_cases = ["aabbbcc", "aabbc", "aaaabc"]

for test in test_cases:
    print("INPUT", test, "OUTPUT", sherlock_valid_string(test))

