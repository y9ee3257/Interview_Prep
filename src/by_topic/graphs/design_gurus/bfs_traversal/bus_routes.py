"""
https://leetcode.com/problems/bus-routes/description/
"""

from collections import defaultdict, deque
from typing import List

class Solution:
    # Method to find the minimum number of buses required to travel from source to target
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        q = deque()
        routes_set = [set(r) for r in routes]
        visited = [False ] *len(routes)

        if source == target:
            return 0

        for route_index, route in enumerate(routes_set):
            if source in route:
                visited[route_index ] =True
                q.append((route_index ,1))
                break


        while q:
            route_index, bus_count = q.popleft()

            if target in routes_set[route_index]:
                return bus_count

            for stop in routes_set[route_index]:
                for index, route in enumerate(routes_set):
                    if not visited[index] and stop in route:
                        q.append((index, bus_count +1))
                        visited[index] = True

        return -1






