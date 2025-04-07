""""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

The LCA of nodes a and b in a tree is defined as the shared ancestor node of a and b that is located farthest from the root of the tree.

Example
Example one

a = 8, b = 9

Output:

5
There are three shared parents of 8 and 9 in this tree: 5, 2, 1. Of those three, the farthest from the root is 5.

Other examples:
LCA(2, 5) = 2
LCA(2, 3) = 1

Notes
A node is considered its own ancestor and its own descendant.
Return the value of the LCA node of the two given nodes.
Constraints:

1 <= number of nodes <= 100000
1 <= node value <= number of nodes
Node values are unique
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

    a_arr =[]
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


