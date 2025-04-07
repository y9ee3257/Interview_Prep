"""
There is a ball in a maze with empty spaces (0) and walls (1). The ball can move up, down, left, or right through empty spaces but won't stop until it hits a wall. When the ball stops, it can change direction.

Given an m x n maze, the ball's start position, and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination. If the ball can't stop at the destination, return false.
Example 1:

Input: start = [0, 4], destination = [0, 1], maze =
 [[0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0],
  [1, 1, 0, 1, 1],
  [0, 0, 0, 0, 0]]

Expected Output: true
Justification: One possible way to stop at the destination is:- left -> down -> left -> up -> right.


Example 2:

Input: start = [0, 3], destination = [4, 4], maze =
   [[0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]]

Expected Output: true
Justification: One possible way to stop at the destination is:- down -> left -> down -> right -> down -> right.


Input: start = [0, 3], destination = [1, 1], maze =
 [[0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0],
  [1, 1, 0, 1, 1],
  [0, 0, 0, 0, 0]]

Expected Output: false
Justification: The ball cannot stop at (1, 1) because it is not hitting the walls.

"""
from collections import deque

class Solution:
    def hasPath(self, maze, start, destination):
        if len(maze) ==0:
            return False

        q = deque([(start[0] ,start[1])])
        m ,n = len(maze), len(maze[0])
        visited = [[0 ] *n for _ in range(m)]
        while q:
            x ,y = q.popleft()
            if x== destination[0] and y == destination[1]:
                return True
            for dir_x, dir_y in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
                new_x, new_y = x + dir_x, y + dir_y
                while 0 <= new_x < m and 0 <= new_y < n and maze[new_x][new_y] != 1:
                    new_x, new_y = new_x + dir_x, new_y + dir_y

                # because it crossed the boundaries, going back to previous location
                new_x, new_y = new_x - dir_x, new_y - dir_y
                if visited[new_x][new_y] == 0:
                    visited[new_x][new_y] = 1
                    q.append((new_x, new_y))

        return False


