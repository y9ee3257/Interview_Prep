"""
https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:

        output = 0

        def add_to_freqmap(val, freq_map):
            if val not in freq_map:
                freq_map[val] = 0
            freq_map[val] += 1

        def remove_from_freqmap(val, freq_map):
            if freq_map[val] == 1:
                del freq_map[val]
            else:
                freq_map[val] -= 1

        def helper(node, freq_map):
            nonlocal output

            if not node:
                return

            add_to_freqmap(node.val, freq_map)

            if not node.left and not node.right:
                count = 0
                for key in freq_map:
                    if freq_map[key] % 2 != 0:
                        count += 1
                if count <= 1:
                    output += 1
                remove_from_freqmap(node.val, freq_map)
                return

            helper(node.left, freq_map)
            helper(node.right, freq_map)

            remove_from_freqmap(node.val, freq_map)

        helper(root, {})
        return output



