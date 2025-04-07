"""
Given a binary tree, list the node values level by level from left to right.
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """


    from collections import deque

    if not root:
        return []

    q = deque()
    q.append(root)
    output = []
    while len(q) > 0:
        row_size = len(q)
        row = []
        for i in range(row_size):
            node = q.popleft()
            row.append(node.value)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        output.append(row)

    return output

