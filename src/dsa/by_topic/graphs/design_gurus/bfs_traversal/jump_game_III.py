"""
https://leetcode.com/problems/jump-game-iii/description/
"""

from collections import deque

class Solution:
    def canReach(self, arr, start):

        q = deque()
        q.append(start)
        while q:
            index = q.popleft()
            if index < 0 or index >= len(arr):
                continue
            if arr[index] < 0:
                continue
            if arr[index] == 0:
                return True

            q.append(index +arr[index])
            q.append(index -arr[index])
            arr[index ] =-arr[index]

        return False
