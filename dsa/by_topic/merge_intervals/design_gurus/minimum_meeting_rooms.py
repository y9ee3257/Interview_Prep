"""
https://neetcode.io/problems/meeting-schedule-ii
https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/problem-challenge-1-minimum-meeting-rooms-hard
"""

import heapq
from collections import deque


# class Meeting:
#  def __init__(self, start, end):
#    self.start = start
#    self.end = end

# You can override/modify __lt__ as per your need
# setattr(Meeting, "__lt__", lambda self, other: write logic here)


class Solution:
    def findMinimumMeetingRooms(self, meetings):

        if not meetings:
            return 0

        minRooms = 1
        meetings.sort(key=lambda x: x.start)

        q = deque([meetings[0]])

        for i in range(1, len(meetings)):
            q.append(meetings[i])
            while q:
                if self.intersect(q[0], meetings[i]):
                    break
                else:
                    q.popleft()
            minRooms = max(minRooms, len(q))
        return minRooms

    def intersect(self, meet1, meet2):
        return meet1.start <= meet2.start < meet1.end or meet2.start <= meet1.start < meet2.end

