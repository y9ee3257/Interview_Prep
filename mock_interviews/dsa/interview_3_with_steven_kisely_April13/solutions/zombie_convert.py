"""
https://leetcode.com/problems/rotting-oranges/description/
https://leetcode.com/discuss/post/411357/amazon-oa-2019-zombie-in-matrix-by-anony-g83r/
"""

from collections import deque


def zombie_convert(matrix):
    if len(matrix) == 0:
        return -1

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    human_count = 0
    q = deque()
    rl = len(matrix)
    cl = len(matrix[0])

    for row_i, row in enumerate(matrix):
        for col_i, cell in enumerate(row):
            if cell == 0:
                human_count += 1
            elif cell == 1:
                q.append((row_i, col_i))

    days = 0

    while q:
        zombie_count = len(q)
        days += 1
        print("day", days, " zombie_count", zombie_count, "human_count", human_count, "q", q)
        for _ in range(zombie_count):
            row, col = q.popleft()

            for dirX, dirY in directions:
                new_row, new_col = row + dirX, col + dirY
                if 0 <= new_row < rl and 0 <= new_col < cl and matrix[new_row][new_col] == 0:
                    matrix[new_row][new_col] = 1
                    q.append((new_row, new_col))
                    human_count -= 1

    if human_count == 0:
        return days - 1

    return -1


arr = [[1, 0, 0, 0, 1],
       [0, 0, 0, 0, 0]]
print(zombie_convert(arr))
arr = [[2, 1],
       [0, 2]]
print(zombie_convert(arr))
arr = [[0, 1, 1, 0, 1],
       [0, 1, 0, 1, 0],
       [0, 0, 0, 0, 1],
       [0, 1, 0, 0, 0]]
print(zombie_convert(arr))
arr = [[1, 0, 0], [0, 0, 2], [2, 0, 0]]
print(zombie_convert(arr))
