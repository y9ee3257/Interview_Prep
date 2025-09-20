"""
https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/conflicting-appointments-medium
"""


# class Interval:
#  def __init__(self, start, end):
#    self.start = start
#    self.end = end

#  def print_interval(self):
#    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class Solution:
    def canAttendAllAppointments(self, intervals):
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)
        last = intervals[0]

        for i in range(1, len(intervals)):
            doesOverlap = intervals[i].start < last.start < intervals[i].end \
                          or last.start < intervals[i].start < last.end
            if doesOverlap:
                return False
            last = intervals[i]

        return True


