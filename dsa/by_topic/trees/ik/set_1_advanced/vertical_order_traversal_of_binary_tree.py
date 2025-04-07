"""
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def vertical_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """

    queue = deque()
    yposition = deque()
    map = {}
    min_depth = 0
    max_depth = 0
    if not root:
        return []

    queue.append(root)
    yposition.append(0)

    while len(queue) > 0:
        current_level_count = len(queue)
        while current_level_count > 0:
            node = queue.popleft()
            y = yposition.popleft()
            if not node:
                current_level_count -= 1
                continue
            max_depth = max(max_depth, y)
            min_depth = min(min_depth, y)

            if y not in map:
                map[y] = []
            map[y].append(node.value)

            queue.append(node.left)
            queue.append(node.right)
            yposition.append(y - 1)
            yposition.append(y + 1)

            current_level_count -= 1

    output = []
    for i in range(min_depth, max_depth + 1):
        output.append(map[i])
    return output
