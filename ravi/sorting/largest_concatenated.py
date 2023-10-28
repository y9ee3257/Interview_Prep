"""
https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/largest-concatenated-number?page=4&pageSize=10

Largest Concatenated Number
Given an array of integers, find the largest number that can be constructed by concatenating all the elements of the given array.

Input Format
The first line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - size of the array and the second line contains N integers - elements of the array.

Output Format
For each test case, print the largest number that can be constructed by concatenating all the elements of the given array, separated by newline.

Constraints
1 <= T <= 1000
1 <= N <= 1000
0 <= ar[i] <= 1000

Example
Input
3
8
49 73 58 30 72 44 78 23
4
69 9 57 60
2
40 4

Output
7873725849443023
9696057
440
"""

import sys
from functools import cmp_to_key

test_cases = int(sys.stdin.readline())


def number_array(number):
    arr = []
    n = number
    while n > 0:
        arr.append(n % 10)
        n = n // 10
    return arr[::-1]


def custom_sort(a, b):
    a_array = number_array(a)
    b_array = number_array(b)
    print(a_array)
    print(b_array)
    for i in range(min(len(a_array), len(b_array))):
        if a_array[i] > b_array[i]:
            return -1
        elif b_array[i] > a_array[i]:
            return 1
    if len(a_array) < len(b_array):
        return -1
    else:
        return 1


for test in range(test_cases):
    length = int(sys.stdin.readline())
    array = [int(x) for x in sys.stdin.readline().split()]
    array.sort(key=cmp_to_key(custom_sort))
    print("".join(map(str, array)))
