"""
https://leetcode.com/problems/find-if-path-exists-in-graph/description/
"""

from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: [[int]], start: int, end: int) -> bool:

        if start==end:
            return True

        graph = defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        if start not in graph:
            return False

        q = deque((list(graph[start])))
        visited = {False for _ in range(n)}
        while q:
            node = q.popleft()
            if node == end:
                return True
            if node not in visited:
                visited.add(node)
                for adj in graph[node]:
                    q.append(adj)

        return False






