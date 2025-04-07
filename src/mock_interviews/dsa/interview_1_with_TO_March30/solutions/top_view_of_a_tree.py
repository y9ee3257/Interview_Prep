"""
https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right =right


from collections import deque

def top_view(tree: TreeNode):
    if not tree:
        return []

    q = deque([(tree, 0)])
    col_map = {} # {1:5, -1:3, -2:2...}
    min_col, max_col = float("inf"), float("-inf")

    while q:
        node, level = q.popleft()
        min_col = min(level,min_col)
        max_col = max(level,max_col)

        if level not in col_map:
            col_map[level] = node.val

        if node.left:
            q.append((node.left, level-1))

        if node.right:
            q.append((node.right, level+1))


    output = []
    for i in range(min_col, max_col+1):
        output.append(col_map[i])


    return output

