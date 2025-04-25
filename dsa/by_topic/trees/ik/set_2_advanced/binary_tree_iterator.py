"""
https://leetcode.com/problems/binary-search-tree-iterator/description/
"""


"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def implement_tree_iterator(root, operations):
    """
    Args:
     root(BinaryTreeNode_int32)
     operations(list_str)
    Returns:
     list_int32
    """
    index = 0
    output = []

    def helper2(value):
        nonlocal index
        while index < len(operations) and operations[index] != "next":
            output.append(1)
            index += 1

        if index < len(operations):
            output.append(value)
            index += 1

    def helper(node):

        if not node:
            return

        left = helper(node.left)
        if left:
            helper2(left.value)

        helper2(node.value)

        right = helper(node.right)

        if right:
            helper2(right.value)

    helper(root)

    while index < len(operations):
        if operations[index] == "next":
            output.append(0)
        else:
            output.append(0)
        index += 1

    return output
