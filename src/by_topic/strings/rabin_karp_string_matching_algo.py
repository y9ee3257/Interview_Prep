# https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/rabin-karp-string-matching-algorithm
#
# Rabin Karp String Matching Algorithm
# Given 2 strings A and B, find the number of occurrences of A in B as a substring.
# Note: Solve using the Rabin-Karp string matching algorithm. Do not use an inbuilt library.
#
# Input Format
# The first line of input contains T - the number of test cases. It's followed by T lines. Each line contains 2 strings - A and B, separated by space.
#
# Output Format
# For each test case, print the number of occurrences of A in B, separated by a new line.
#
# Constraints
# 30 points
# 1 <= len(A), len(B) <= 1000
#
# 70 points
# 1 <= len(A), len(B) <= 10000
#
# General Constraints
# 1 <= T <= 2000
# 'a' <= A[i], B[i] <= 'z'
#
# Example
# Input
# 4
# smart yekicmsmartplrplsmartrplplmrpsmartrpsmartwmrmsmartsmart
# interviews interviewseiwcombvinterviewskrenlzp
# ds dsdsajdsrjjdsjjj
# algo yalgoalgoalgopalgoaxalgoasaxalgolalgoalgoalgo
#
# Output
# 6
# 2
# 4
# 9


import sys

test_cases = int(sys.stdin.readline())

for test_case in range(test_cases):
    inputs = sys.stdin.readline().split()
    pattern = inputs[0]
    main_string = inputs[1]
    base = 7  # any random prime number
    pattern_hash = 0
    # create hash for pattern a,b,c,d = a*base^3 + b*base^2 + c*base^1 + d
    for idx, char in enumerate(pattern):
        pattern_hash += ord(char) * pow(base, len(pattern) - idx - 1)
    left = 0
    right = 0
    substring_hash = 0
    occurences = 0
    while right <= len(main_string):
        # initial hash calculation for k elements
        if right < len(pattern):
            substring_hash += ord(main_string[right]) * pow(base, len(pattern) - right - 1)
            right += 1
        else:
            # if pattern matches, compare both strings
            if substring_hash == pattern_hash and pattern == main_string[left:right]:
                occurences += 1
            if right < len(main_string):
                # calculate hash for removing left character
                substring_hash -= ord(main_string[left]) * pow(base, len(pattern) - 1)
                # increasing the base power for remaining characters
                substring_hash *= base
                # add right character
                substring_hash += ord(main_string[right]) * pow(base, 0)
            left += 1
            right += 1

    print(occurences)
