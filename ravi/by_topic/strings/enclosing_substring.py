# https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/enclosing-substring
#
# Enclosing Substring
# Given 2 strings A and B, find the smallest substring of B having all the characters of A, in any order.
# Input Format
# The first line of input contains T - the number of test cases. It's followed by T lines,
# each line containing 2 space-separated strings - A and B.
# Output Format
# For each test case, print the length of the smallest substring of B having all the characters of A,
# separated by newline. If no such substring is found, print -1.
#
# Constraints
# 20 points
# 1 <= T <= 100
# 1 <= size(A), size(B) <= 100

# 60 points
# 1 <= T <= 100
# 1 <= size(A), size(B) <= 1000

# 120 points
# 1 <= T <= 100
# 1 <= size(A), size(B) <= 10000

# General Constraints
# 'a' <= A[i],B[i] <= 'z'

# Example
# Input
# 4
# fkqyu frqkzkruqmfqyuzlkyg
# onmwvytbytn uqhmfjaqtgngcwkuzyamnerphfmw
# bloets lwbcrsfothplxseplrtbshbtstjloxsf
# dzpd dclzztpjldkndgbdqqzmbp
#
# Output
# 7
# -1
# 13
# 9

import sys

test_cases = int(sys.stdin.readline())

for test_case in range(test_cases):
    inputs = sys.stdin.readline().split()
    string_b, string_a = inputs[0], inputs[1]

    string_b_map = {}
    for char in string_b:
        string_b_map[char] = string_b_map.get(char, 0)

    left, right = 0, 0
    tmp_map = string_b_map
    current_map = {}
    for idx, char in enumerate(string_a):
        if char in string_b_map:
            current_map[char] = current_map.get(char, 0) + 1
            tmp_map.pop(char)
        if len(tmp_map) == 0:
            right = idx
            break
    while right <= len(string_a) - 1 and right - left + 1 >= len(string_b):
        left_char = string_a[left]
        right_char = string_a[right]
        if current_map.get(left_char, 0) == 1:
            if left_char == right_char:
                left += 1
            else:

                right += 1
        else:
            if left_char in current_map:
                current_map[left_char] = current_map[left_char] - 1
            left += 1
