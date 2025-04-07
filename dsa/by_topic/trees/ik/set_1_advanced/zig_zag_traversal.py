
"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def zigzag_level_order_traversal(root):
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
    is_even_level = False
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
        if is_even_level:
            row.reverse()
        output.append(row)
        is_even_level = not is_even_level

    return output
