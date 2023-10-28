"""
https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/sort-0s-and-1s?page=4&pageSize=10

Sort 0s and 1s
You are given an array of 0's and 1's. Sort the array in ascending order and print it.
Note: Solve using two-pointer technique.

Input Format
The first line of input contains T - the number of test cases. Its followed by 2T lines, the first line contains N - the size of the array. The second line contains the elements of the array.

Output Format
For each test case, sort the array in ascending order and print it on a new line.

Constraints
1 <= T <= 1000
1 <= N <= 1000
0 <= A[i] <= 1

Example
Input
2
5
0 1 1 0 1
6
1 1 1 1 1 0

Output
0 0 1 1 1
0 1 1 1 1 1
"""

import sys

test_cases = int(sys.stdin.readline())

for test in range(test_cases):
    length = int(sys.stdin.readline())
    array = [int(x) for x in sys.stdin.readline().split()]
    p1 = 0
    p2 = length - 1
    while p1 < p2:
        if array[p1] == 1 and array[p2] == 0:
            array[p1] = 0
            array[p2] = 1
            p1 += 1
            p2 -= 1
            continue
        if array[p1] != 1:
            p1 += 1
        if array[p2] != 0:
            p2 -= 1
    print(" ".join(map(str, array)))
