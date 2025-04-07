"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
"""

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[n-1][n-1]==1:
            return -1
        q = deque([(0, 0, 1)])
        output = -1

        target = len(grid) - 1
        visited = [[False] * n for _ in range(n)]

        def validate_and_add(x, y, steps):
            if 0 <= x <= target and 0 <= y <= target and grid[x][y] != 1 and not visited[x][y]:
                q.append((x, y, steps))

        while q:
            x, y, steps = q.popleft()
            if x == y == target:
                output = steps if output == -1 else min(output, steps)
                continue

            for i in {-1, 1}:
                # horizonatal
                validate_and_add(x + i, y, steps + 1)
                # vertical
                validate_and_add(x, y + i, steps + 1)
                # diagonal
                validate_and_add(x + i, y + i, steps + 1)
                validate_and_add(x - i, y + i, steps + 1)

            visited[x][y] = True

        return output
