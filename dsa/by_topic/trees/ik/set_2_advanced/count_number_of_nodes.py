"""
https://leetcode.com/problems/count-complete-tree-nodes/description/
"""


"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def count_nodes(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """

    def countheight(node, isLeft):
        count = 0
        while node:
            node = node.left if isLeft else node.right
            count+=1
        return count

    def helper(node):
        if not node:
            return 0

        leftH= countheight(node, True)
        rightH = countheight(node,False)

        if leftH == rightH:
            return pow(2,leftH)-1

        left = helper(node.left)
        right = helper(node.right)

        return left+right+1

    return helper(root)




"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
# Initial implementation (not optimal)
def count_nodes(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    if not root:
        return 0

    leaf_count = 0
    max_height = None
    def helper(node, level):
        nonlocal leaf_count, max_height

        if not node.left and not node.right:
            if not max_height:
                max_height = level
            if level == max_height:
                leaf_count+=1
                return True
            return False

        if node.left:
            should_continue = helper(node.left, level+1)
        if should_continue and node.right:
            should_continue = helper(node.right,level+1)

        return should_continue

    helper(root,1)

    return pow(2,max_height-1)-1 + leaf_count
