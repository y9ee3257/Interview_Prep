"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
"""



"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def construct_binary_tree(inorder, preorder):
    """
    Args:
     inorder(list_int32)
     preorder(list_int32)
    Returns:
     BinaryTreeNode_int32
     "inorder": [3, 2, 1, 5, 4, 6],
     "preorder": [1, 2, 3, 4, 5, 6]

     "inorder": [2, 1, 3],
     "preorder": [1, 2, 3]
    """
    inmap = {}
    for index,value in enumerate(inorder):
        inmap[value]=index


    def helper(start_i,end_i,start_p,end_p):
        if start_i < 0 or end_i >= len(inorder) or start_p <0 or end_p >= len(preorder) or start_i > end_i or start_p > end_p:
            return

        if start_i == end_i:
            return BinaryTreeNode(inorder[start_i])


        rootValue = preorder[start_p] # 1
        inorderIndex = inmap[rootValue] # 1

        left_len = inorderIndex - start_i  # 1
        right_len = end_i - inorderIndex # 1

        start_p_l, end_p_l =  start_p+1, start_p+left_len # 1, 1
        start_p_r, end_p_r = end_p_l+1, end_p # 2, 2


        root = BinaryTreeNode(rootValue)
        root.left = helper(start_i,inorderIndex-1, start_p_l, end_p_l) # 0, 0, 1,1
        root.right = helper(inorderIndex+1,end_i, start_p_r, end_p_r) # 2, 2, 2,2

        return root

    return helper(0, len(inorder)-1, 0, len(preorder)-1)




