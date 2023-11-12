"""
https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/two-set-bits?page=2&pageSize=10

Two Set Bits
Look at the following sequence:
3, 5, 6, 9, 10, 12, 17, 18, 20....
All the numbers in the series have exactly 2 bits set in their binary representation. Your task is simple, you have to find the Nth number of this sequence.

Input Format
The first line of input contains T - the number of test cases. It's followed by T lines, each containing a single number N.

Output Format
For each test case, print the Nth number of the sequence, separated by a newline. Since the number can be very large, print the number % 1000000007.

Constraints
30 points
1 <= T, N <= 200

70 points
1 <= T, N <= 105

100 points
1 <= T <= 105
1 <= N <= 1014

Example
Input
5
1
2
5
50
100
Output
3
5
10
1040
16640
"""

import sys

test_cases = sys.stdin.readline()

for test in range(int(test_cases)):
    num = int(sys.stdin.readline())
    n = 1
    while n * (n + 1) // 2 < num:
        n += 1
    prev_total = n * (n - 1) // 2
    x = num - prev_total - 1
    print((pow(2, n) + pow(2, x)) % 1000000007)
