
"""
https://www.interviewkickstart.com/blogs/problems/binary-tree-postorder-traversal
or
https://codestandard.net/articles/binary-tree-postorder-traversal/
"""


"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def postorder_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """

    stack = []
    output = []

    stack.append(root)

    while len(stack)>0:
        current = stack.pop()
        output.append(current.value)

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    output.reverse()
    return output
