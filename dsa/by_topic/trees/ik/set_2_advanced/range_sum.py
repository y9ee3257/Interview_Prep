"""
https://leetcode.com/problems/range-sum-of-bst/description/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def get_range_sum(root, low, high):
    """
Args:
root(BinaryTreeNode_int32)
low(int32)
high(int32)
Returns:
int32
"""

    sum = 0
    def helper(node):
        nonlocal sum

        if not node:
            return

        if low <= node.value <= high:
            sum += node.value

        if not node.value < low:
            helper(node.left)
        if not node.value > high:
            helper(node.right)


    helper(root)
    return sum