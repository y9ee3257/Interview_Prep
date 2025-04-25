"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
"""
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def nodes_at_given_distance(root, target_node, distance):
    """
    Args:
     root(BinaryTreeNode_int32)
     target_node(int32)
     distance(int32)
    Returns:
     list_int32
    """
    parent_map = {}
    target=None

    def parent_mapper(node, parent):
        nonlocal target
        if not node:
            return

        parent_map[node.value] = parent
        parent_mapper(node.left,node)
        parent_mapper(node.right,node)

        if node.value == target_node:
            target = node

    parent_mapper(root, None)

    visited=set()
    output = []

    def helper(node, dist):
        if not node:
            return

        if dist == distance:
            output.append(node.value)
            return

        visited.add(node.value)

        if node.left and node.left.value not in visited:
            helper(node.left,dist+1)
        if node.right and node.right.value not in visited:
            helper(node.right,dist+1)
        if parent_map[node.value] and parent_map[node.value].value not in visited:
            helper(parent_map[node.value],dist+1)

    helper(target, 0)
    return output







# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # store the parents of all nodes, so you can use the BT as a graph
        parent_map = {}
        q = deque([(None,root)])
        while q:
            parent, node = q.popleft()
            parent_map[node.val] = parent
            if node.left:
                q.append((node,node.left))
            if node.right:
                q.append((node,node.right))

        q = deque([(target,0)])
        visited = set()
        output =[]
        while q:
            node, distance = q.popleft()
            parent = parent_map[node.val]
            if distance == k:
                output.append(node.val)
            if node.left and node.left.val not in visited:
                q.append((node.left, distance+1))
            if node.right and node.right.val not in visited:
                q.append((node.right, distance+1))
            # treating this as a graph, iterating through parent as well
            if parent and parent.val not in visited:
                q.append((parent, distance+1))
            visited.add(node.val)

        return output