"""
https://leetcode.com/problems/is-graph-bipartite
"""

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]


        def find_parent(a):
            x = a
            while parent[x] != x:
                x = parent[x]
            parent[a] = x
            return x

        def join(a,b):
            pa = find_parent(a)
            pb = find_parent(b)
            if pa == pb:
                return

            if rank[pa] > rank[pb]:
                parent[b] = pa
                rank[a] = rank[a] + rank[b]
            else:
                parent[a] = pb
                rank[b] = rank[a] + rank[b]

        for i in range(n):
            adj_nodes = graph[i]
            if not adj_nodes:
                continue
            first_node = adj_nodes[0]
            for adj in adj_nodes:
                if find_parent(i) == find_parent(adj):
                    return False
                join(first_node, adj)

        return True

