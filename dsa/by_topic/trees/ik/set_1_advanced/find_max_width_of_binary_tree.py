"""
https://leetcode.com/problems/maximum-width-of-binary-tree/description/
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
def find_maximum_width(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """

    q = deque([(root,0)])
    max_width = 0

    while q:
        row_len = len(q)
        left, right = 0, 0
        for i in range(row_len):
            node, pos = q.popleft()

            # left is initiated to 0, taking just min(left,pos) will never be updated
            left = min(left, pos) if left else pos
            right = max(right,pos)

            if node.left:
                q.append((node.left, 2*pos+1))
            if node.right:
                q.append((node.right, 2*pos+2))

        max_width = max(max_width,right-left+1)

    return max_width


