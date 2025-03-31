"""
https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1
"""

# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

class Solution:
    def bottomView(self, root):
        # Function to return the top view of the binary tree.
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

                index_map[index] = node.val

                if node.left:
                    q.append((node.left, index -1))
                if node.right:
                    q.append((node.right, index +1))

        for index in range(min_index, max_index +1):
            topViewNodes.append(index_map[index])

        return topViewNodes
