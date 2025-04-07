"""
https://www.geeksforgeeks.org/boundary-traversal-of-binary-tree/
"""

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val

#         self.left = left
#         self.right = right
#
#  get left boundary
#  get leaves in order
#  get right boundary (in reverse order)
#
class Solution2:
    def boundaryOfBinaryTree(self, root):
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        nodes_arr = [root.val]

        def collect_left_boundary(node):
            if not node:
                return

            if node.left or node.right:
                nodes_arr.append(node.val)

            if node.left:
                collect_left_boundary(node.left)
            else:
                collect_left_boundary(node.right)

        def collect_right_boundary(node):
            if not node:
                return

            if node.right:
                collect_right_boundary(node.right)
            else:
                collect_right_boundary(node.left)

            if node.left or node.right:
                nodes_arr.append(node.val)

        def collect_leaves(node):
            if not node:
                return

            if not node.left and not node.right:
                nodes_arr.append(node.val)

            if node.left:
                collect_leaves(node.left)
            if node.right:
                collect_leaves(node.right)

        collect_left_boundary(root.left)
        collect_leaves(root)
        collect_right_boundary(root.right)
        return nodes_arr


# Takes time to get to this approach, it's join of all the 3 functions in the above approach
class Solution1:
    def boundaryOfBinaryTree(self, root):
        if not root:
            return []

        nodes_arr = [root.val]

        def helper(node, direction, is_boundary):
            if not node:
                return
            if not node.left and not node.right:
                nodes_arr.append(node.val)
                return

            if is_boundary:
                nodes_arr.append(node.val)

            if direction == "left":
                if node.left:
                    helper(node.left, direction, is_boundary)
                if node.right:
                    helper(node.right, direction, is_boundary and not node.left)
            else:
                if node.right:
                    helper(node.right, direction, is_boundary)
                if node.left:
                    helper(node.left ,direction, is_boundary and not node.right)

        helper(root.left, "left", True)

        output = nodes_arr[:]
        nodes_arr = []

        helper(root.right, "right", True)

        output += nodes_arr[::-1]

        return output


