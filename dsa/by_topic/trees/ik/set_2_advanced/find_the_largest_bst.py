"""
https://takeuforward.org/data-structure/largest-bst-in-binary-tree
https://leetcode.com/problems/largest-bst-subtree/description/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def find_largest_bst(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """

    max_bst = 0

    def helper(root):
        nonlocal max_bst
        if not root:
            return (True, 0, None, None)

        is_l_valid, l_nodes, l_min, l_max = helper(root.left)
        is_r_valid, r_nodes, r_min, r_max = helper(root.right)

        default = root.value
        l_min = l_min or default
        l_max = l_max or default
        r_min = r_min or default
        r_max = r_max or default

        sub_trees_valid = is_l_valid and is_r_valid
        check_left = not root.left or root.left.value <= root.value
        check_right = not root.right or root.right.value >= root.value
        check_sub_values = l_max <= root.value <= r_min

        is_valid = sub_trees_valid and check_left and check_right and check_sub_values
        node_count = l_nodes + r_nodes + 1

        if is_valid:
            max_bst = max(max_bst, node_count)

        return (is_valid, node_count, l_min, r_max)

    helper(root)
    return max_bst
