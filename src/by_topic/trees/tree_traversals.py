"""
Given a binary tree, return the output in array format for the below tree traversals
1. Pre Order Traversal
2. In Order Traversal
3. Post Order Traversal
4. Level Order Traversal
5. Standard Array Representation where you can find the children of node "n" at (2n+1, 2n+2)
"""

from collections import deque


# Tree Traversal Methods
def inorder_traversal(root):
    output = []

    def helper(node):
        if not node:
            return
        output.append(node.val)
        helper(node.left)
        helper(node.right)

    helper(root)
    return output


def preorder_traversal(root):
    output = []

    def helper(node):
        if not node:
            return
        helper(node.left)
        output.append(node.val)
        helper(node.right)

    helper(root)
    return output


def postorder_traversal(root):
    output = []

    def helper(node):
        if not node:
            return
        helper(node.left)
        helper(node.right)
        output.append(node.val)

    helper(root)
    return output


def level_order_traversal(root):
    q = deque()
    q.append(root)
    output = []
    while q:
        node = q.popleft()
        output.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return output


def tree_to_array(root):
    q = deque()
    q.append((root, 0))
    output = []
    while q:
        (node, index) = q.popleft()
        for _ in range(len(output),index):
            output.append("X")
        output.append(node.val)
        if node.left:
            q.append((node.left, 2 * index + 1))
        if node.right:
            q.append((node.right, 2 * index + 2))
    return output


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Visual Representation:
#          8
#        /   \
#       4     12
#      / \   /  \
#     2   6 10   14
#    /   /   \   \
#   1   5    11   13

# Level 0 (Root)
root = TreeNode(8)
# Level 1
root.left = TreeNode(4)
root.right = TreeNode(12)
# Level 2
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.left = TreeNode(10)
root.right.right = TreeNode(14)
# Level 3 (Some nodes are null)
root.left.left.left = TreeNode(1)
root.left.left.right = None  # Null node
root.left.right.left = TreeNode(5)
root.left.right.right = None  # Null node
root.right.left.left = None  # Null node
root.right.left.right = TreeNode(11)
root.right.right.left = TreeNode(13)
root.right.right.right = None  # Null node

# Array Representation of Tree (Complete Binary Tree Representation)
tree_array = [8, 4, 12, 2, 6, 10, 14, 1, None, 5, None, None, 11, 13, None]

print(inorder_traversal(root))
print(preorder_traversal(root))
print(postorder_traversal(root))
print(level_order_traversal(root))
print(tree_to_array(root))