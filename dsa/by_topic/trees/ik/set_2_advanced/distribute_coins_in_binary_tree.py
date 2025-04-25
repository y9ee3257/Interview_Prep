"""
https://leetcode.com/problems/distribute-coins-in-binary-tree/description/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def get_minimum_moves(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """

    moves = 0
    def helper(node):
        nonlocal moves

        if not node:
            return 0

        left = helper(node.left)
        right = helper(node.right)

        coin_diff = left + right + node.value -1

        moves += abs(coin_diff)
        return coin_diff

    helper(root)

    return moves
