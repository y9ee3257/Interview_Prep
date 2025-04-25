"""
https://leetcode.com/problems/binary-tree-right-side-view/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
from collections import deque


def right_view(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    q = deque([root])
    output = []
    while q:
        row_len = len(q)
        node = None
        for i in range(row_len):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        output.append(node.value)
    return output
