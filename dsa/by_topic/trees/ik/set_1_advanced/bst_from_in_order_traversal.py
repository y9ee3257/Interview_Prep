"""
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def build_binary_search_tree(preorder):
    """
    Args:
     preorder(list_int32)
    Returns:
     BinaryTreeNode_int32
    """

    index = 0

    def helper(low, high):
        nonlocal index
        if index >= len(preorder) or preorder[index] > high or preorder[index] < low:
            return
        value = preorder[index]
        node = BinaryTreeNode(value)
        index += 1
        node.left = helper(low, value)
        node.right = helper(value, high)

        return node

    return helper(float("-inf"), float("inf"))
