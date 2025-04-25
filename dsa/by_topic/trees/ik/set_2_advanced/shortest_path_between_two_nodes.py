"""
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def shortest_path(root, start_node_value, end_node_value):
    """
    Args:
     root(BinaryTreeNode_int32)
     start_node_value(int32)
     end_node_value(int32)
    Returns:
     str
    """
    startPath = []
    endPath = []
    def helper(node, slate, char):
        nonlocal startPath, endPath
        if not node:
            return
        slate.append(str(node.value)+char)
        if node.value == start_node_value:
            startPath = slate[:]
        if node.value == end_node_value:
            endPath = slate[:]

        helper(node.left, slate, "L")
        helper(node.right,slate, "R")
        slate.pop()

    helper(root, [], "")

    i=0
    while i< len(startPath) and i<len(endPath) and startPath[i] == endPath[i]:
        i+=1

    output = []

    for u in range(i,len(startPath)):
        output.append("U")

    for d in range(i,len(endPath)):
        output.append(endPath[d][-1])

    return "".join(output)


