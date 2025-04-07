"""
https://leetcode.com/problems/keys-and-rooms/description/
"""


# using BFS
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms):
        q = deque([0])
        visited = set()

        while q:
            room = q.popleft()
            if room in visited:
                continue
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    q.append(key)

        return len(visited) == len(rooms)


# using DFS
class Solution:
    def canVisitAllRooms(self, rooms):
        visited = set()
        def helper(room):
            if room in visited:
                return
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    helper(key)
        helper(0)
        return len(visited) == len(rooms)
