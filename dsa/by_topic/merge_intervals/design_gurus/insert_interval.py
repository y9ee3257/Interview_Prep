"""
https://leetcode.com/problems/insert-interval/description/
https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/insert-interval-medium
"""

import heapq


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        heap = []
        heapq.heappush(heap, newInterval)
        i = 0
        while heap:
            if i < len(intervals):
                heapq.heappush(heap, intervals[i])
                i += 1

            top = heapq.heappop(heap)
            if res and top[0] <= res[-1][1]:
                res[-1][1] = max(top[1], res[-1][1])
            else:
                res.append(top)

        return res


# class Interval:
#  def __init__(self, start, end):
#    self.start = start
#    self.end = end

class Solution:
    def insert(self, intervals, new_interval):
        merged = []
        # TODO: Write your code here
        intervals.sort(key = lambda x: x.start)
        for interval in intervals:
            if not merged:
                merged.append(interval)

            if self.overlapping(interval, merged[-1]):
                merged[-1 ] =self.merge(interval ,merged[-1])
            else:
                merged.append(interval)

            if new_interval:
                if self.overlapping(new_interval, merged[-1]):
                    merged[-1 ] =self.merge(new_interval ,merged[-1])
                    new_interval =None
                elif new_interval.end < merged[-1].start:
                    last = merged.pop()
                    merged.append(new_interval)
                    merged.append(last)
                    new_interval =None

        if new_interval:
            merged.append(new_interval)
        return merged


    def overlapping(self ,int1, int2):
        return int2.start <= int1.start <= int2.end or int1.start <= int2.start <= int1.end

    def merge(self ,int1, int2):
        int1.start = min(int1.start ,int2.start)
        int1.end = max(int1.end ,int2.end)
        return int1