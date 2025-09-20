"""
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
"""

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        nodes_with_incoming_edges = set()

        for edge in edges:
            nodes_with_incoming_edges.add(edge[1])

        baselist = []
        for i in range(n):
            if i not in nodes_with_incoming_edges:
                baselist.append(i)

        return baselist

