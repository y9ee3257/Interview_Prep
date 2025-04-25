"""
https://leetcode.com/problems/balanced-binary-tree/
"""


"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def is_height_balanced(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     bool
    """


    def helper(node):
        if not node:
            return (0, True)

        lh, is_left = helper(node.left)
        rh, is_right = helper(node.right)

        return (max(lh, rh)+1, is_left and is_right and abs(lh-rh) <=1)


    height, is_balanced = helper(root)
    return is_balanced