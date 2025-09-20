# """
# Given 2 strings str1 and str2. Generate all permutations of str1 using recursion and return true if str2 is a permutation of str1.
# Example:
# str1 = “abcd”
# str2 = “dacb”
# result = checkPermutation(str1, str2)
# True
# str1 = “abcd”
# str2 = “waka”
# result = checkPermutation(str1, str2)
# False
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase english letters only
#
# [a,b,c,d]
#
# a
# b
# c
# d
# _   _   _   _
# 4   3   2   1
# """
#
# def generatePermutations(string1, string2):
#     permutations = set()
#     slate = []
#     def recursion(slate, remaining):
#         if len(slate) == len(string1):
#             permutations.add(slate[:])
#             return
#
#         for idx,char in enumerate(remaining):
#             slate.append(char)
#             recursion(slate, remaining[:idx]+remaining[idx+1:])
#             slate.pop()
#
#     for idx, char in enumerate(string1):
#         slate.append(char)
#         recursion(slate, string1[:idx]+string1[idx+1:])
#         slate.pop()
#
#     return string2 in permutations
#
#
#
# """
# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.
#
# Example:
#    2              1
#   /  \          /   \
#  1    4        0     3
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
#
# Example 2:
# 1           8
#  \         /
#   8       1
# Input: root1 = [1, null, 8], root2 = [8, 1]
# Output: [1,1,8,8]
# """
#
#
# def traverse(tree1, tree2):
#     res1, res2 = [],[]
#     def inorder(root, res):
#         if not root:
#             return
#         inorder(root.left)
#         res.add(root.value, res)
#         inorder(root.right)
#
#     inorder(tree1, res1)
#     inorder(tree2, res2)
#
#     l,r = 0, 0
#     result = []
#     while l < len(res1) and r< len(res2):
#         if res1[l] <= res2[r]:
#             result.append(res1[l])
#             l+=1
#         else:
#             result.append(res2[r])
#             r+=1
#
#     while l < len(res1):
#         result.append(res1[l])
#     while r < len(res2):
#         result.append(res2[r])
#
#     return result
#


"""
Given two non-negative integers, num1 and num2 represented as strings, 
return the sum of num1 and num2 as a string

You must solve the problem without using any build-in library for handling
large integers (such as BigInteger). You must also not convert (Cast) the inputs
to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:
1 <= num1.length, num2.length <= 1000
num1 and num2 consist of only digits
num1 and num2 don't have any leading zeros except for the number zero

"6" "7"

1. somehow convert them to binary and add
ord("7")
"""
# print(ord("0")-ord("0"))
# print(ord("1")-ord("0"))
# print(ord("2")-ord("0"))

# Input: num1 = "19", num2 = "123"
# Output: "134"
def add(str1,str2):
    remainder = 0
    l,r = len(str1)-1,len(str2)-1

    def intValue(char):
        return ord(char)-ord("0")

    sum = []
    while l>=0 or r>=0:
        total = remainder
        if l>=0:
            total+=intValue(str[l])
        if r>=0:
            total += intValue(str[r])

        if total > 9:
            sum.append(total-10)
            remainder = 1
        else:
            sum.append(total)
            remainder=0

    return "".join(sum[::-1])

"""
Implement the "paint fill" function that one might see on many image editing programs that is given a screen (represented by a 2-dimensional array of colors), a point, and a new color fill in the surrounding area (up, down, left, right) until the color changes from the original color.

# screen is the 2d matrix
# x, y are your starting row, colomn,
# ncolor is the new color

Example:
Starting at 1, 1 and ncolor is green,
[[red, blue, blue],
 [red, blue, green],
 [blue, blue, red],
]
The end result is
[[red, green, green],
 [red, green, green],
 [green, green, red],
]

"""
from collections import deque
def paintFill(screen, x, y, ncolor):
    if not screen:
        return screen
    rows = len(screen)
    cols = len(screen[0])

    visited = [[0 for _ in cols] for _ in rows]

    color = screen[x][y]
    q = deque()
    q.append((x,y))
    while q:
        curx,cury = q.popleft()
        visited[curx][cury] =1
        if screen[curx][cury] == color:
            screen[curx][cury] = ncolor

        for dir in [(1,0),(-1,0),(0,1),(1,0)]:
            if visited[dir[0]][dir[1]] == 0:
                q.append(dir)

    return screen




