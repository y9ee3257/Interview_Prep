"""
https://leetcode.com/problems/max-area-of-island/description/
"""

from collections import deque
class Solution:
    def maxAreaOfIsland(self, matrix):
        biggestIslandArea = 0
        if len(matrix)==0:
            return 0
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        for row in range(self.rows):
            for col in range(self.cols):
                if matrix[row][col] == 1 and not self.visited[row][col]:
                    area = self.helper(row,col,matrix)
                    biggestIslandArea = max(biggestIslandArea, area)

        return biggestIslandArea

    def helper(self,row,col,matrix):
        q = deque([(row,col)])
        count = 0
        while q:
            x, y = q.popleft()

            if 0<=x<self.rows and 0<=y<self.cols and not self.visited[x][y] and matrix[x][y]==1:
                count+=1
                self.visited[x][y] = True
                q.append((x+1,y))
                q.append((x,y+1))
                q.append((x-1,y))
                q.append((x,y-1))
        return count
