"""
https://leetcode.com/problems/merge-intervals/
https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/merge-intervals-medium
"""


# class Interval:
#  def __init__(self, start, end):
#    self.start = start
#    self.end = end

#  def print_interval(self):
#    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        return res


class Solution:
    def merge(self, intervals):
        mergedIntervals = []
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            if not mergedIntervals:
                mergedIntervals.append(interval)

            if interval.start <= mergedIntervals[-1].end:
                mergedIntervals[-1].end = max(interval.end, mergedIntervals[-1].end)
            else:
                mergedIntervals.append(interval)

        return mergedIntervals
