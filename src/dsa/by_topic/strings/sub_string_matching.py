# https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/substring-matching
#
# Substring Matching
# You are given two strings A and B. You are also given Q queries with 4 indices i, j, k, and l.
# Check whether the substring of A[i:j] matches the substring of B[k:l].
#
# Input Format
# The first line of input contains T - the number of test cases. In each test case,
# the first line contains the string A and the second line contains the string B.
# The next line contains an integer Q - the number of queries.
# The Q subsequent lines each contain 4 integers i, j, k, and l, separated by a space.
#
# Output Format
# For each query, on a new line, print "Yes" if the substring of A matches the substring of B, print "No" otherwise.
#
# Constraints
# 30 points
# 1 <= T <= 100
# 1 <= len(A), len(B) <= 100
# 0 <= Q <= 1000
#
# 120 points
# 1 <= T <= 100
# 1 <= len(A), len(B) <= 10000
# 0 <= Q <= 10000
# General Constraints
# 'a' <= A[i], B[i] <= 'z'
# 0 <= i <= j < len(A)
# 0 <= k <= l < len(B)
#
# Example
# Input
# 2
# smartinterviews
# intermediate
# 2
# 5 9 0 4
# 1 3 2 4
# hackerrank
# hackerearth
# 1
# 0 3 0 3
#
# Output
# Yes
# No
# Yes
#
# Explanation
# Test-Case 1
# The substring of "smartinterviews" from index 5 to 9 is "inter".
# The substring of "intermediate" from 0 to 4 is also "inter". Since these both are equal, the output is "Yes".
# The substring of "smartinterviews" from index 1 to 3 is "mar".
# The substring of "intermediate" from 2 to 4 is "ter". Since these both are not equal, the output is "No".


import sys



