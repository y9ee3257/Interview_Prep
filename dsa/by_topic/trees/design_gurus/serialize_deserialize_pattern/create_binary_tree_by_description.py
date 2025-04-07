"""
https://leetcode.com/problems/create-binary-tree-from-descriptions/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        map = {}
        root_nodes = set()

        for desc in descriptions:
            parent, child, isLeft = desc[0], desc[1], desc[2]

            if parent not in map:
                map[parent] = TreeNode(parent)
                root_nodes.add(parent)

            childNode = None

            if child in map:
                childNode = map[child]
                root_nodes.remove(child)
            else:
                childNode = TreeNode(child)
                map[child] = childNode

            if isLeft == 1:
                map[parent].left = childNode
            else:
                map[parent].right = childNode

        return map[root_nodes.pop()]
