"""
Given a binary tree, return all paths from root to leaf.
            1
           /\
          2  3
         /\  /\
       4  5 6  7
[
[1, 2, 4],
[1, 2, 5],
[1, 3, 6],
[1, 3, 7]
]
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def all_paths_of_a_binary_tree(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32

    Bottom up approach
    """
    if not root:
        return []

    output = []

    def helper(slate, node):
        if not node.left and not node.right:
            output.append(slate[:])
            return

        if node.left:
            slate.append(node.left.value)
            helper(slate, node.left)
            slate.pop()
        if node.right:
            slate.append(node.right.value)
            helper(slate, node.right)
            slate.pop()

    helper([root.value], root)
    return output

