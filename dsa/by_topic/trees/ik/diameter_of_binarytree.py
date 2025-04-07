"""
Given a binary tree, find its diameter.

Diameter of a binary tree is the length of the longest path between any two nodes of the tree.
Length between any two nodes is equal to the number of edges traversed to reach one node from the other.

        5
       / \
     4    3
     \     \
      2     1
 diameter for th above is 4 (number of edges between 2 and 1)
 i.e. traversing from 2-4, 4-5, 5-3, 3-1
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def binary_tree_diameter(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """

    max_diameter = 0
    def helper(node):
        nonlocal max_diameter
        if not node:
            return 0

        left_height = helper(node.left)
        right_height = helper(node.right)
        max_diameter = max(max_diameter, left_height + right_height)
        return max(left_height,right_height) + 1

    helper(root)
    return max_diameter




