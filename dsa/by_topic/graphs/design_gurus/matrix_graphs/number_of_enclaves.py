"""
https://leetcode.com/problems/number-of-enclaves/
"""

from collections import deque
class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        canreach = [[False for _ in range(cols)] for _ in range(rows)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        q = deque()
        for i in range(rows):
            q.append((i,0))
            q.append((i,cols-1))
        for j in range(cols):
            q.append((0,j))
            q.append((rows-1,j))

        while q:
            print(q)
            row, col = q.popleft()
            if 0<=row<rows and 0<=col<cols and grid[row][col]==1 and not canreach[row][col]:
                canreach[row][col]=True
                for d in directions:
                    q.append((row+d[0],col+d[1]))

        count =0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not canreach[i][j]:
                    count+=1

        return count


