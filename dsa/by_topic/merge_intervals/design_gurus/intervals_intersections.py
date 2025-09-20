"""
https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/intervals-intersection-medium
"""


# class Interval:
#  def __init__(self, start, end):
#    self.start = start
#    self.end = end


class Solution:
    def merge(self, intervals_a, intervals_b):
        result = []
        a, b = 0, 0
        while a < len(intervals_a) and b < len(intervals_b):
            inta, intb = intervals_a[a], intervals_b[b]
            if self.overlap(inta, intb):
                result.append(Interval(max(inta.start, intb.start), min(inta.end, intb.end)))
            if inta.end < intb.end:
                a += 1
            else:
                b += 1
        return result

    def overlap(self, inta, intb):
        return intb.start <= inta.start <= intb.end or inta.start <= intb.start <= inta.end

