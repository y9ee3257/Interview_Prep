"""
https://leetcode.com/problems/check-completeness-of-a-binary-tree/
"""

from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def complete_binary_tree(root: TreeNode):
    if not root:
        return True
    q = deque([root])
    output = []
    while q:
        node = q.popleft()
        output.append(node.val if node else None)
        if node:
            q.append(node.left)
            q.append(node.right)

    while output[-1] == None:
        output.pop()

    for node in output:
        if not node:
            return False

    return True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

## print(complete_binary_tree(root))
