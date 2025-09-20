"""
https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/problem-challenge-2-maximum-cpu-load-hard
"""

from heapq import *
from collections import deque


# class job:
#  def __init__(self, start, end, cpu_load):
#    self.start = start
#    self.end = end
#    self.cpuLoad = cpu_load

# You can override/modify __lt__ as per your need
# setattr(Job, "__lt__", lambda self, other: write logic here)

class Solution:
    def findMaxCPULoad(self, jobs):
        maxLoad = 0
        if not jobs:
            return 0

        jobs.sort(key=lambda x: x.start)
        q = deque([jobs[0]])
        currentLoad = jobs[0].cpuLoad

        for i in range(1, len(jobs)):
            q.append(jobs[i])
            currentLoad += jobs[i].cpuLoad

            while q[0].end < jobs[i].start:
                top = q.popleft()
                currentLoad -= top.cpuLoad

            maxLoad = max(maxLoad, currentLoad)

        return maxLoad

    def overlapping(self, int1, int2):
        return int1.start <= int2.start <= int1.end or int2.start <= int1.start <= int2.end


class Solution2:
    def findMaxCPULoad(self, jobs):
        maxLoad = 0
        if not jobs:
            return 0

        jobs.sort(key=lambda x: x.start)
        q = deque([jobs[0]])
        currentLoad = jobs[0].cpuLoad

        for i in range(1, len(jobs)):

            while q:
                if self.overlapping(jobs[i], q[0]):
                    break
                else:
                    top = q.popleft()
                    currentLoad -= top.cpuLoad

            q.append(jobs[i])
            currentLoad += jobs[i].cpuLoad

            maxLoad = max(maxLoad, currentLoad)

        return maxLoad

    def overlapping(self, int1, int2):
        return int1.start <= int2.start <= int1.end or int2.start <= int1.start <= int2.end




