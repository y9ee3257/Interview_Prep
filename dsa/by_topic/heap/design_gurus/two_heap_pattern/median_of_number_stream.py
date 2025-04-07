"""
https://leetcode.com/problems/find-median-from-data-stream/
"""

from heapq import *

class Solution:

    def __init__(self):
        self.min_heap =[]
        self.max_heap = []

    def insertNum(self, num: int) -> None:
        if len(self.max_heap) > 0 and num <= -self.max_heap[0]:
            heappush(self.max_heap,-num)
        else:
            heappush(self.min_heap,num)

        if len(self.min_heap) - len(self.max_heap) > 1:
            heappush(self.max_heap, -heappop(self.min_heap))
        elif len(self.max_heap) - len(self.min_heap) > 1:
            heappush(self.min_heap, -heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return float(self.min_heap[0]) if len(self.min_heap) > len(self.max_heap) else float(-self.max_heap[0])