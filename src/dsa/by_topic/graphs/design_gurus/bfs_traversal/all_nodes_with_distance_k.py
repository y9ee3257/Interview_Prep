"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
"""
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
        q = deque([(None ,root)])
        while q:
            parent, node = q.popleft()
            parent_map[node.val] = parent
            if node.left:
                q.append((node ,node.left))
            if node.right:
                q.append((node ,node.right))

        q = deque([(target ,0)])
        visited = set()
        output =[]
        while q:
            node, distance = q.popleft()
            parent = parent_map[node.val]
            if distance == k:
                output.append(node.val)
            if node.left and node.left.val not in visited:
                q.append((node.left, distance + 1))
            if node.right and node.right.val not in visited:
                q.append((node.right, distance + 1))
            # treating this as a graph, iterating through parent as well
            if parent and parent.val not in visited:
                q.append((parent, distance + 1))
            visited.add(node.val)

        return output






