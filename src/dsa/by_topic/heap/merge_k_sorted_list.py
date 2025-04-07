# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import Optional, List
from queue import PriorityQueue

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    start_node = ListNode(0)
    output = start_node
    pq = PriorityQueue()
    for idx, lst in enumerate(lists):
        if lst:
            pq.put((lst.val, idx, lst))
    while not pq.empty():
        (val, idx, lst) = pq.get()
        if lst.next:
            pq.put((lst.next.val, idx, lst.next))
        output.next = ListNode(val)
        output = output.next

    return start_node.next



input = ListNode(20, ListNode())






