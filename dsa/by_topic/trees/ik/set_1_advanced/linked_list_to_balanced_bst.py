"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
"""

"""
For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def sorted_list_to_bst(head):
    """
    Args:
     head(LinkedListNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    if not head:
        return
    if not head.next:
        return BinaryTreeNode(head.value)

    length = 0
    curr_head = head
    while curr_head:
        curr_head = curr_head.next
        length += 1

    curr_head = head
    prev = None
    for i in range(length // 2):
        prev = curr_head
        curr_head = curr_head.next
    if prev:
        prev.next = None

    node = BinaryTreeNode(curr_head.value)
    node.left = sorted_list_to_bst(head)
    node.right = sorted_list_to_bst(curr_head.next)

    return node
