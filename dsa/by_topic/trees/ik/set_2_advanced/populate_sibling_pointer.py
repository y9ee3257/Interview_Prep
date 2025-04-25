"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next_right = None
"""


def populate_sibling_pointers(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """

    from collections import deque

    if not root:
        return root

    q = deque([root])

    while q:
        row_len = len(q)
        prev = None
        for _ in range(row_len):
            curr = q.popleft()
            if prev:
                prev.next_right = curr

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

            prev = curr

    return root
