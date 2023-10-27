"""
https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/balanced-parentheses?page=3&pageSize=10

Balanced Parentheses
Write a program to generate all possible strings with balanced parentheses having N pairs of curly braces.

Input Format
The first line of input contains T - the number of test cases. It's followed by T lines, each containing a single integer N.

Output Format
For each test case, print each combinational pair of balanced parenthesis of length N in a lexicographical order along with the test case number, separated by a new line.

Constraints
1 <= T <= 12
1 <= N <= 12

Example
Input
2
3
2

Output
Test Case #1:
{{{}}}
{{}{}}
{{}}{}
{}{{}}
{}{}{}
Test Case #2:
{{}}
{}{}
"""

import sys

test_cases = sys.stdin.readline()


def backtracking(open_count, close_count, index, ouput):
    if open_count == 0 and close_count == 0:
        print("".join(output))
        return

    if 0 < open_count <= close_count:
        output[index] = "{"
        backtracking(open_count - 1, close_count, index + 1, output)

    if close_count > 0 and close_count >= open_count:
        output[index] = "}"
        backtracking(open_count, close_count - 1, index + 1, output)
    return


for test_case in range(int(test_cases)):
    n = int(sys.stdin.readline())
    output = [None] * n * 2
    print(f"Test Case #{test_case + 1}:")
    backtracking(n, n, 0, output)
