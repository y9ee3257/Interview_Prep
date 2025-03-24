"""
Given a binary tree, check if it is a binary search tree (BST). A valid BST does not have to be complete or balanced.

Consider this definition of a BST:

All nodes values of left subtree are less than or equal to parent node value.
All nodes values of right subtree are greater than or equal to parent node value.
Both left subtree and right subtree must be BSTs.
NULL tree is a BST.
Single node trees (including leaf nodes of any tree) are BSTs.
Example One
Example one

Output:

0
Left child value 200 is greater than the parent node value 100; violates the definition of BST.

Example Two
Example two

Output:

1
Notes
Return true if the input tree is a BST or false otherwise.
Constraints:

0 <= number of nodes <= 100000
-109 <= values stored in the nodes <= 109




For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def is_bst(root):

    def helper(node, upper_limit, lower_limit):
        if not node:
            return True

        if not (lower_limit <= node.value <= upper_limit):
            return False

        return helper(node.left, node.value, lower_limit) and helper(node.right, upper_limit, node.value)

    return helper(root, float("inf"), float("-inf"))

