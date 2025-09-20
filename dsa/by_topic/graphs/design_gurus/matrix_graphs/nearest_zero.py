"""
https://leetcode.com/problems/01-matrix/description/
"""

from collections import deque

class Solution:
    def updateMatrix(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        visited = [[False for _ in range(cols)]for _ in range(rows)]

        q = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visited[i][j]=True

        level = 0
        while q:
            for _ in range(len(q)):
                row,col= q.popleft()
                mat[row][col] = level

                for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                    new_r, new_c = row+dr, col+dc
                    if 0<=new_r<rows and 0<=new_c<cols and not visited[new_r][new_c]:
                        visited[new_r][new_c] = True
                        q.append((new_r,new_c))
            level+=1

        return mat



