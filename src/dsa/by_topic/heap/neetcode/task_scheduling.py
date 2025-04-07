"""
https://neetcode.io/problems/task-scheduling
"""

from collections import Counter
from heapq import heapify, heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [(-freq[key],0, key) for key in freq]
        heapify(heap)
        output, tempq =[], []
        while heap:
            for i in range(n+1):
                if len(heap) == 0:
                    if len(tempq) ==0: break
                    output.append("-")
                    continue
                count, priority, char = heappop(heap)
                count = -count
                output.append(char)
                if count > 1:
                    heappush(tempq,(1-count, i-n, char))

            for i in range(len(tempq)):
                heappush(heap,heappop(tempq))

        return len(output)


#  same solution as above but O(1) space
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [(-freq[key],0, key) for key in freq]
        heapify(heap)
        output, tempq =0, []
        while heap:

            for i in range(n+1):
                if len(heap) == 0:
                    if len(tempq) ==0: break
                    output+=1
                    continue
                count, priority, char = heappop(heap)
                count = -count
                output+=1
                if count > 1:
                    heappush(tempq,(1-count, i-n, char))

            for i in range(len(tempq)):
                heappush(heap,heappop(tempq))

        return output



















































