"""
https://leetcode.com/problems/symmetric-tree/description/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
from collections import deque
def check_if_symmetric(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     bool
    """
    if not root:
        return True

    def helper(node1, node2):
        # when both nodes are null, return True
        if not node1 and not node2:
            return True

        # when only one node is null, return False, if values are not equal, return False
        if not node1 or not node2 or node1.value != node2.value:
            return False

        return helper(node1.left, node2.right) and helper(node1.right,node2.left)



    return helper(root.left,root.right)







