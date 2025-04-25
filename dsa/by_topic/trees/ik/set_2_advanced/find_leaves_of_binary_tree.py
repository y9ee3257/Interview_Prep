"""
https://algo.monster/liteproblems/366
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def find_leaves(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """

    output = []

    def helper(node):
        if not node:
            return -1

        left = helper(node.left)
        right = helper(node.right)

        curr_level = max(left, right) + 1

        if curr_level >= len(output):
            output.append([node.value])
        else:
            output[curr_level].append(node.value)

        return curr_level

    helper(root)
    return output
