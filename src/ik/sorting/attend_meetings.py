# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/


# using sorting
# time complexity O(nlogn)
# space complexity O(1)
def can_attend_all_meetings(intervals):
    intervals.sort(key=lambda x: x[0])
    prev_end = -1
    for idx in range(len(intervals)):
        start = intervals[idx][0]
        end = intervals[idx][1]
        if start >= prev_end:
            prev_end = end
        else:
            return 0
    return 1
