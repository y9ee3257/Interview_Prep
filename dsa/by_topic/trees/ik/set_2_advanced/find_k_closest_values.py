"""
https://interviewkickstart.com/blogs/problems/closest-values-in-bst
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
from heapq import *


def find_k_closest_values(root, target, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     target(int32)
     k(int32)
    Returns:
     list_int32
    """

    top_k = []

    def helper(node):
        if not node:
            return

        heappush(top_k, (-abs(target - node.value), node.value))

        while len(top_k) > k:
            heappop(top_k)

        helper(node.left)
        helper(node.right)

    helper(root)

    output = [value for diff, value in top_k]

    return output
