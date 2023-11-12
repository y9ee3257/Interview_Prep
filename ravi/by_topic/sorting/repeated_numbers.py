"""
https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/repeated-numbers?page=2&pageSize=10

Repeated Numbers
You are given an array of N elements. All elements of the array are in range 1 to N-2. All elements occur once except two numbers, which occur twice. Your task is to find the two repeating numbers.
Input Format
The first line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - the size of the array and second line contains the elements of the array.
Output Format
Print the 2 repeated numbers in sorted manner, for each test case, separated by new line.
Constraints
30 points
1 <= T <= 100
4 <= N <= 103
70 points
1 <= T <= 100
4 <= N <= 106
Example
Input
2
8
1 3 2 3 4 6 5 5
10
1 5 2 8 1 4 7 4 3 6
Output
3 5
1 4
"""
import sys

test_cases = int(sys.stdin.readline())

for test in range(test_cases):
    length = sys.stdin.readline()
    array = [int(x) for x in sys.stdin.readline().split()]
    output = []
    for element in array:
        if array[abs(element) - 1] < 0:
            output.append(abs(element))
        else:
            array[abs(element) - 1] = -array[abs(element) - 1]
    output.sort()
    print(" ".join(map(str, output)))
