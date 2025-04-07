"""
https://www.geeksforgeeks.org/flip-binary-tree/
"""


"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def flip_upside_down(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    if not root:
        return None

    new_tree = BinaryTreeNode(None)

    def helper(node):
        if not node.left and not node.right:
            new_tree.value = node.value
            return new_tree

        curr_root = helper(node.left)

        curr_root.left = BinaryTreeNode(node.right.value)
        curr_root.right = BinaryTreeNode(node.value)
        return curr_root.right

    helper(root)
    return new_tree