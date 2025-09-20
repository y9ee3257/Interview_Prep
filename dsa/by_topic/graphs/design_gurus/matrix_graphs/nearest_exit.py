"""
https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
"""

from collections import deque


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        if len(maze) == 0:
            return -1

        rows = len(maze)
        cols = len(maze[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        q = deque([(0, entrance[0], entrance[1])])

        while q:
            count, x, y = q.popleft()

            if (x == 0 or y == 0 or x == rows - 1 or y == cols - 1) and (x != entrance[0] or y != entrance[1]):
                return count

            visited[x][y] = True

            for x1, y1 in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_x, new_y = x + x1, y + y1
                if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y] and maze[new_x][new_y] == '.':
                    q.append((count + 1, new_x, new_y))

        return -1


from collections import deque


