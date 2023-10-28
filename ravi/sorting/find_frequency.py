"""
https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/finding-frequency?page=5&pageSize=10

Given an array, you have to find the frequency of a number x.
Input Format
The first line of input contains N - size of the array. The next line contains N integers, the elements of the array.
The next line contains Q - number of queries. Each of the next Q lines contains a single integer X,
for which you have to find the frequency of X in the given array.
Output Format
For each query, print the frequency of X, separated by newline.

Constraints
30 points
1 <= N <= 105
1 <= Q <= 102
-108 <= ar[i] <= 108
70 points
1 <= N <= 105
1 <= Q <= 105
-108 <= ar[i] <= 108

Example
Input
9
-6 10 -1 20 -1 15 5 -1 15
5
-1
10
8
15
20
Output
3
1
0
2
1

Solve using:
a. Sort + 1BS + Expand
b. Sort + 2BS
c. Sort + Compress to A,B + BS
d. Sort array + Sort queries + 2-pointer + BS in original queries
e. Inbuilt HashMap Library
"""

import sys

array_size = int(sys.stdin.readline())
array = sys.stdin.readline().split(" ")
dict = {}
for element in array:
    element_int = int(element)
    if element_int not in dict:
        dict[element_int] = 1
    else:
        dict[element_int] += 1

queries = int(sys.stdin.readline())

for query in range(queries):
    input_num = int(sys.stdin.readline())
    if input_num in dict:
        print(dict[input_num])
    else:
        print(0)
