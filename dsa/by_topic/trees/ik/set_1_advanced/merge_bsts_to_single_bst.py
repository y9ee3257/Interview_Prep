"""
https://leetcode.com/problems/merge-bsts-to-create-single-bst/description/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def merge_two_binary_search_trees(root1, root2):
    """
    Args:
     root1(BinaryTreeNode_int32)
     root2(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """

    def in_order_traversal(root, output):
        if not root:
            return

        in_order_traversal(root.left, output)
        output.append(root.value)
        in_order_traversal(root.right, output)

    def merge_two_sorted_arrays(arr1, arr2):
        p1, p2 = 0, 0
        output = []
        while p1 < len(arr1) and p2 < len(arr2):
            if arr1[p1] < arr2[p2]:
                output.append(arr1[p1])
                p1 += 1
            else:
                output.append(arr2[p2])
                p2 += 1

        while p1 < len(arr1):
            output.append(arr1[p1])
            p1 += 1
        while p2 < len(arr2):
            output.append(arr2[p2])
            p2 += 1

        return output

    def construct_bst(arr, start, end):
        if start > end or start > len(arr) - 1:
            return None
        if start == end:
            return BinaryTreeNode(arr[start])

        mid = start + (end - start) // 2
        node = BinaryTreeNode(arr[mid])
        node.left = construct_bst(arr, start, mid - 1)
        node.right = construct_bst(arr, mid + 1, end)
        return node

    arr1 = []
    arr2 = []
    in_order_traversal(root1, arr1)
    in_order_traversal(root2, arr2)
    sorted_array = merge_two_sorted_arrays(arr1, arr2)
    return construct_bst(sorted_array, 0, len(sorted_array))
