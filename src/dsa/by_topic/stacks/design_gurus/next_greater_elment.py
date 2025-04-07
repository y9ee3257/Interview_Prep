"""
Problem Statement
Given an array, print the Next Greater Element (NGE) for every element.

The Next Greater Element for an element x is the first greater element on the right side of x in the array.

Elements for which no greater element exist, consider the next greater element as -1.

Examples
Example 1:

 Input: [4, 5, 2, 25]
 Output: [5, 25, 25, -1]
Example 1:

 Input: [13, 7, 6, 12]
 Output: [-1, 12, 12, -1]
Example 1:

 Input: [1, 2, 3, 4, 5]
 Output: [2, 3, 4, 5, -1]
Constraints:

1 <= arr.length <= 104
-109 <= arr[i] <= 109

"""

class Solution:
    def nextLargerElement(self, arr):
        res = [-1] * len(arr)
        stack = []
        for idx, num in enumerate(arr):
            while len(stack) > 0 and stack[-1][0] < num:
                (_, i) = stack.pop()
                res[i] = num
            stack.append((num, idx))
        return res
