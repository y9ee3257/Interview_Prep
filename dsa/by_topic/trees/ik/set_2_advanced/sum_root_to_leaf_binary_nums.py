"""
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/
"""



"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def sum_root_to_leaf_numbers(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """

    output = []

    def helper(node,slate):
        if not node:
            return

        slate.append(str(node.value))

        if not node.left and not node.right:
            output.append(int("".join(slate),2))
            slate.pop()
            return

        helper(node.left, slate)
        helper(node.right, slate)
        slate.pop()

    helper(root,[])
    return sum(output)

