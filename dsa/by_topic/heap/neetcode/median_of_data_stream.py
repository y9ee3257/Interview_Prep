"""
https://neetcode.io/problems/find-median-in-a-data-stream
"""



from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.min_heap =[]
        self.max_heap = []
    """
    maintain two heaps, one for min heap and one for max heap
    push, elements to min/max heaps based on their value
    balance them every time
    """
    def addNum(self, num: int) -> None:
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
            return self.min_heap[0] if len(self.min_heap) > len(self.max_heap) else -self.max_heap[0]

