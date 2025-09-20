"""
https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/problem-challenge-3-employee-free-time-hard
"""



import heapq
#class Interval:
#    def __init__(self, start, end):
#        self.start = start
#        self.end = end


# Time : O(Nlogk)
# Given all the working hours are sorted, use heapq to push in the one interval at a time from all employee schedules
class Solution:
    def findEmployeeFreeTime(self, schedule):
        if not schedule:
            return []

        heap = []
        for i, sch in enumerate(schedule):
            heapq.heappush(heap, (sch[0], i, 0))

        workingHours = []
        while heap:
            interval, employeeIndex, intervalIndex = heapq.heappop(heap)
            if workingHours and interval.start <= workingHours[-1].end:
                workingHours[-1].end = max(interval.end, workingHours[-1].end)
            else:
                workingHours.append(interval)

            if intervalIndex + 1 < len(schedule[employeeIndex]):
                newVal = (schedule[employeeIndex][intervalIndex + 1], employeeIndex, intervalIndex + 1)
                heapq.heappush(heap, newVal)

        res = []
        for i in range(1, len(workingHours)):
            res.append([workingHours[i - 1].end, workingHours[i].start])
        return res



# Time : O(NlogN)
class Solution2:
    def findEmployeeFreeTime(self, schedule):
        result = []

        ws = schedule[0]
        for i in range(1 ,len(schedule)):
            ws = self.getCommonWH(ws, schedule[i])

        for i in range(1 ,len(ws)):
            result.append([ws[ i -1].end, ws[i].start])

        return result

    def getCommonWH(self, sch1, sch2):

        sch = sch1 + sch2
        sch.sort(key = lambda x: x.start)

        res = [sch[0]]
        for i in range(1 ,len(sch)):
            if sch[i].start <= res[-1].end:
                res[-1].end = max(res[-1].end ,sch[i].end)
            else:
                res.append(sch[i])

        return res
