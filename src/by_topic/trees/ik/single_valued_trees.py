"""
https://leetcode.com/problems/univalued-binary-tree/description/


For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
count = 0
def find_single_value_trees2(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    helper(root, None)
    return count

def helper(node, parent_value):
    global count
    if not node:
        return True

    left_value = helper(node.left,node.value)
    right_value = helper(node.right,node.value)

    if left_value and right_value:
        count+=1

    return node.value == parent_value and left_value and right_value


def find_single_value_trees2(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """

    count = [0]

    def helper(node):
        if not node:
            return True

        is_left = helper(node.left)
        is_right = helper(node.right)

        if is_left and is_right and (not node.left or node.left.value == node.value) and (
                not node.right or node.right.value == node.value):
            count[0] += 1
            return True
        else:
            return False

    helper(root)
    return count[0]

class BinaryTreeNode:
    def __init__(self, value ,left=None ,right=None):
        self.value = value
        self.left = left
        self.right = right

left = BinaryTreeNode(5, BinaryTreeNode(5), BinaryTreeNode(5))
right = BinaryTreeNode(5, BinaryTreeNode(4), BinaryTreeNode(5))
print(find_single_value_trees(BinaryTreeNode(5, left, right)))