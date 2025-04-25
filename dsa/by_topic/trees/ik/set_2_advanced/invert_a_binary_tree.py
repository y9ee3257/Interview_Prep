"""
https://leetcode.com/problems/invert-binary-tree/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def mirror_image(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     Nothing
    """

    if not root:
        return
    root.left, root.right = root.right, root.left
    mirror_image(root.left)
    mirror_image(root.right)
    return root
