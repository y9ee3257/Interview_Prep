"""
https://leetcode.com/problems/all-paths-from-source-to-target/description/
"""

from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        target = len(graph)-1
        def helper(node,path):
            if node == target:
                result.append(path[:]+[node])
                return
            path.append(node)
            for adj_node in graph[node]:
                helper(adj_node, path)
            path.pop()
        helper(0,[])
        return result
