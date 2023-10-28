"""
https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/lcm-and-hcf?page=0&pageSize=10

LCM and HCF
Given 2 numbers, find their LCM and HCF.
Note: Do not use any inbuilt functions/libraries for your main logic. Read about the Euclid Algorithm to solve the problem.

Input Format
The first line of input contains T - the number of test cases. It's followed by T lines, each contains 2 numbers A and B.

Output Format
For each test case, print their LCM and HCF separated by space, separated by a new line.

Constraints
1 <= T <= 105
1 <= A,B <= 109

Example
Input
4
4 710
13 1
6 4
605904 996510762

Output
1420 2
13 1
12 2
7740895599216 78
"""

import sys

test_cases = int(sys.stdin.readline())


#    m = n*multiple + reminder
def gcd(m, n):
    reminder = m % n
    if reminder == 0:
        return n
    return gcd(n, reminder)


# m*n = gcd*lcm
for test in range(test_cases):
    inputs = [int(x) for x in sys.stdin.readline().split()]
    m = inputs[0]
    n = inputs[1]
    gcd = gcd(m, n) if m > n else gcd(n, m)
    lcm = (m * n) // gcd
    print(lcm, gcd)
