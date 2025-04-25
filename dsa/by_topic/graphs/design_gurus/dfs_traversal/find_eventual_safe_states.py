"""
https://leetcode.com/problems/find-eventual-safe-states/description/
"""


class Solution:
    def eventualSafeNodes(self, graph):
        visited = set()
        safe = set()

        def helper(node):
            is_safe = True
            visited.add(node)

            for adj_node in graph[node]:
                if adj_node not in visited:
                    is_safe = is_safe and helper(adj_node)
                elif adj_node not in safe:
                    is_safe = False

            if is_safe:
                safe.add(node)
            return is_safe

        for i in range(len(graph)):
            helper(i)

        result = list(safe)
        result.sort()
        return result  # Sorting the result
