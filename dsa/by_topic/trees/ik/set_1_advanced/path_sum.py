"""
https://leetcode.com/problems/path-sum-ii/description/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def all_paths_sum_k(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
    Returns:
     list_list_int32
    """

    output = []
    def helper(slate,node,total):
        if not node.left and not node.right:
            if total+node.value == k:
                output.append(slate[:]+[node.value])
            return

        slate.append(node.value)
        if node.left:
            helper(slate,node.left,total+node.value)
        if node.right:
            helper(slate,node.right,total+node.value)
        slate.pop()

    helper([],root,0)
    if not output:
        return [[-1]]
    return output