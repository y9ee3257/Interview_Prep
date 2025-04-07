"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def lca(root, a, b):
    """
    Args:
     root(BinaryTreeNode_int32)
     a(BinaryTreeNode_int32)
     b(BinaryTreeNode_int32)
    Returns:
     int32
    """

    if not root:
        return None

    a_arr = []
    b_arr = []

    def helper(slate, node):
        nonlocal a_arr, b_arr
        if not node:
            return

        slate.append(node.value)

        if node.value == a.value:
            a_arr = slate[:]

        if node.value == b.value:
            b_arr = slate[:]

        helper(slate, node.left)
        helper(slate, node.right)

        slate.pop()

    helper([], root)

    result = None
    for i in range(min(len(a_arr), len(b_arr))):
        if a_arr[i] != b_arr[i]:
            break
        result = a_arr[i]

    return result
