"""
https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1
"""
import collections


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # Function to return the top view of the binary tree.
    def topView(self, root):
        # Result list to store the top view nodes.
        if not root:
            return []

        topViewNodes = []
        q = collections.deque()
        q.append((root ,0))

        index_map = {}
        min_index, max_index = 0, 0

        while q:
            row_len = len(q)
            for _ in range(row_len):
                (node, index) = q.popleft()
                min_index = min(min_index, index)
                max_index = max(max_index, index)

                if index not in index_map:
                    index_map[index] = node.val

                if node.left:
                    q.append((node.left, index -1))
                if node.right:
                    q.append((node.right, index +1))

        for index in range(min_index, max_index +1):
            topViewNodes.append(index_map[index])

        return topViewNodes






