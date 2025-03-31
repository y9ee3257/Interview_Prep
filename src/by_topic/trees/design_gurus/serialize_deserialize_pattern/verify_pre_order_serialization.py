"""
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
"""


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        input_arr = preorder.split(",")

        if preorder == "#":
            return True

        count = 0

        for i, val in enumerate(input_arr):
            if i != 0 and count == 0:
                return False
            if val == "#":
                count -= 1
            else:
                count += 2 if i == 0 else 1

        return count == 0



class Solution2:
    def isValidSerialization(self, preorder: str) -> bool:
        count = 1
        for val in preorder.split(","):
            if count == 0: return False
            count += -1 if val == "#" else 1
        return count == 0
