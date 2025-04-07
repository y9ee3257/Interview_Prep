# https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/stock-span?page=11&pageSize=10
#
# Stock Span
#
# You are given a series of daily price quotes for a stock and you need to calculate the span of the stock’s price for each day. The span Si of the stock’s price on the current day i is defined as the maximum number of consecutive days just before the current day[including the current day], on which the price of the stock is less than or equal to its price on the current day.
#
#
#
# Input Format
#
# The first line of input contains T - the number of test cases. It is followed by 2T lines, the first line contains N - the size of the array. The second line contains N integers - the elements of the array, ith element denotes the stock price on ith day.
#
#
#
# Output Format
#
# For each test case, print a space-separated Stock Span Array, separated by a new line.
#
#
#
# Constraints
#
# 30 points
#
# 1 <= T <= 100
#
# 1 <= N <= 103
#
#
#
# 70 points
#
# 1 <= T <= 200
#
# 1 <= N <= 104
#
#
#
# General Constraints
#
# 0 <= A[i] <= 104
#
#
#
# Example
#
# Input
#
# 2
#
# 7
#
# 100 80 60 70 60 75 85
#
# 10
#
# 0 7 3 6 6 9 18 0 16 0
#
#
#
# Output
#
# 1 1 1 2 1 4 6
#
# 1 2 1 2 3 6 7 1 2 1

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import deque

test_cases = int(sys.stdin.readline())
# 0 7 3 6 6 9 18 0 16 0
for test_case in range(test_cases):
    length = int(sys.stdin.readline())
    array = [int(x) for x in sys.stdin.readline().split(" ")]
    stack = deque()
    output = []
    for idx, num in enumerate(array):
        while len(stack) > 0 and array[stack[len(stack) - 1]] <= num:
            stack.pop()
        stack.append(idx)
        if len(stack) == 1:
            output.append(idx + 1)
        else:
            output.append(idx - stack[len(stack) - 2])
    print(" ".join(map(str, output)))
