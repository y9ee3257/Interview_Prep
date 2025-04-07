"""
Given a stack, sort it using only stack operations (push and pop).

You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The values in the stack are to be sorted in descending order, with the largest elements on top.

Examples
1. Input: [34, 3, 31, 98, 92, 23]
   Output: [3, 23, 31, 34, 92, 98]

2. Input: [4, 3, 2, 10, 12, 1, 5, 6]
   Output: [1, 2, 3, 4, 5, 6, 10, 12]

3. Input: [20, 10, -5, -1]
   Output: [-5, -1, 10, 20]
"""


class Solution:
    def sortStack(self, stack):
        temp_stack = []
        temp_stack2 = []

        for element in stack:
            while temp_stack and temp_stack[-1] > element:
                temp_stack2.append(temp_stack.pop())
            temp_stack.append(element)
            while temp_stack2 > 0:
                temp_stack.append(temp_stack2.pop())

        return temp_stack
