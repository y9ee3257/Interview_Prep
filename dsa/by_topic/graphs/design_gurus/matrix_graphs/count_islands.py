"""
https://leetcode.com/problems/number-of-islands/
"""

from collections import deque


class Solution:
    def countIslands(self, matrix):
        totalIslands = 0
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])

        visited = [[0 for _ in range(n)] for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 1 and visited[row][col] == 0:
                    totalIslands += 1
                    q = deque([(row, col)])
                    while q:
                        print(q)
                        print(visited)
                        r, c = q.popleft()
                        visited[r][c] = 1
                        for x, y in directions:
                            r1, c1 = r + x, c + y
                            if 0 <= r1 < m and 0 <= c1 < n and visited[r1][c1] == 0 and matrix[r1][c1] == 1:
                                q.append((r1, c1))

        return totalIslands
