


# using BFS
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms):
        q = deque([0])
        visited = [False] * len(rooms)

        while q:
            room = q.popleft()
            if visited[room]:
                continue

            visited[room] = True
            for key in rooms[room]:
                if not visited[key]:
                    q.append(key)

        for room in visited:
            if not room:
                return False
        return True


# using DFS