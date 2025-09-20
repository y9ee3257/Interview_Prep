"""
https://leetcode.com/problems/pacific-atlantic-water-flow/
"""

from collections import deque
class Solution:
    def pacificAtlantic(self, matrix):

        rows = len(matrix)
        cols = len(matrix[0])
        pq = deque()
        aq = deque()
        pacific = [[False for _ in range(rows)] for _ in range(cols)]
        atlantic = [[False for _ in range(rows)] for _ in range(cols)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(rows):
            pacific[i][0] = True
            atlantic[i][cols-1]=True
            pq.append((i,0))
            aq.append((i,cols-1))
        for j in range(cols):
            pacific[0][j] = True
            atlantic[rows-1][j] = True
            pq.append((0,j))
            aq.append((rows-1,j))

        while pq:
            row, col = pq.popleft()
            for d in directions:
                new_r,new_c = row+d[0], col+d[1]
                if 0<=new_r<rows and 0<=new_c<cols and not pacific[new_r][new_c] and matrix[new_r][new_c] >= matrix[row][col]:
                    pacific[new_r][new_c] = True
                    pq.append((new_r,new_c))
        while aq:
            row, col = aq.popleft()
            for d in directions:
                new_r,new_c = row+d[0], col+d[1]
                if 0<=new_r<rows and 0<=new_c<cols and not atlantic[new_r][new_c] and matrix[new_r][new_c] >= matrix[row][col]:
                    atlantic[new_r][new_c] = True
                    aq.append((new_r,new_c))

        output = []
        for i in range(rows):
            for j in range(cols):
                if atlantic[i][j] and pacific[i][j]:
                    output.append([i,j])

        return output



