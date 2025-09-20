"""
https://neetcode.io/problems/top-k-elements-in-list
"""

from collections import Counter
from heapq import heapify, heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []

        freq = Counter(nums)
        heap = []
        for key in freq.keys():
            heappush(heap,(-freq[key],key))

        output = []
        for i in range(k):
            output.append(heappop(heap)[1])

        return output










