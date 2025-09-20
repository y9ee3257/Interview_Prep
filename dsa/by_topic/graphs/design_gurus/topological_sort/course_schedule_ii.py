"""
https://leetcode.com/problems/course-schedule-ii/description/
"""


from collections import deque, defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        map = defaultdict(list)
        # must initialize with all nodes or else the source nodes will be missing as they have 0 indegree
        indegree = {i:0 for i in range(numCourses)}
        for edge in prerequisites:
            map[edge[0]].append(edge[1])
            indegree[edge[1]]+=1

        output = []
        q = deque()
        for key in indegree.keys():
            if indegree[key]==0:
                q.append(key)

        while q:
            source = q.popleft()
            output.append(source)
            for adj in map[source]:
                indegree[adj]-=1
                if indegree[adj]==0:
                    q.append(adj)

        if len(output) == numCourses:
            return output[::-1]
        return []
