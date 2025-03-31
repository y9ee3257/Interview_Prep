"""
https://leetcode.com/problems/shortest-path-with-alternating-colors/description/
"""

from collections import deque, defaultdict

# Standard BFS solution
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        edge_map = {"R": defaultdict(set), "B": defaultdict(set)}
        # convert edge list to map
        for vertex, edge in redEdges:
            edge_map["R"][vertex].add(edge)
        for vertex, edge in blueEdges:
            edge_map["B"][vertex].add(edge)

        q = deque([(0, "R", 0), (0, "B", 0), ])
        output = [-1] * n
        visited = {"R": set(), "B": set()}
        while q:
            node, color, steps = q.popleft()
            output[node] = steps if output[node] == -1 else min(steps, output[node])
            next_color = "R" if color == "B" else "B"

            if node in visited[color] or node not in edge_map[next_color]:
                continue

            visited[color].add(node)
            for edge in edge_map[next_color][node]:
                if edge not in visited[next_color]:
                    q.append((edge, next_color, steps + 1))
        return output


# My Initial Implementation
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        answer = []
        edge_map = {"R": defaultdict(set), "B": defaultdict(set)}
        # convert edge list to map
        for vertex, edge in redEdges:
            edge_map["R"][vertex].add(edge)
        for vertex, edge in blueEdges:
            edge_map["B"][vertex].add(edge)
        for target_index in range(n):
            visited = {"R": set(), "B": set()}
            q = deque([(0, 'R', 0), (0, 'B', 0)])
            final_steps = -1
            while q:
                (node, color, step) = q.popleft()
                if node == target_index:
                    final_steps = step
                    break
                visited[color].add(node)
                for edge in edge_map[color][node]:
                    if edge not in visited[color]:
                        q.append((edge, "R" if color == "B" else "B", step + 1))
            answer.append(final_steps)
        return answer
