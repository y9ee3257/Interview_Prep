"""
https://neetcode.io/problems/valid-tree
"""

from collections import defaultdict, deque
class Solution:
    def validTree(self, n, edges):

        map = defaultdict(set)

        for edge in edges:
            edge.sort()
            map[edge[0]].add(edge[1])

        q = deque(list(map[0]))
        visited = {0}
        while q:
            node = q.popleft()
            if node in visited:
                return False

            visited.add(node)

            for adj in map[node]:
                q.append(adj)

        for i in range(n):
            if i not in visited:
                return False

        return True


