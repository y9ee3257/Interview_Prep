"""
https://leetcode.com/problems/possible-bipartition/
"""

from collections import defaultdict, deque


class Solution:
    # Using Disjoint Sets/ Union Find
    def possibleBipartition(self, n, dislikes):
        uf = UnionFind()
        map = defaultdict(set)
        for a, b in dislikes:
            map[a].add(b)
            map[b].add(a)

        for i in range(1, n + 1):
            adj_nodes = list(map[i])
            if not adj_nodes:
                continue
            first_node = adj_nodes[0]
            for adj in adj_nodes:
                if uf.find(i) == uf.find(adj):
                    return False
                uf.union(first_node, adj)
        return True


class UnionFind:

    def __init__(self):
        self.parent = {}
        self.rank = defaultdict(lambda: 1)

    def find(self, a):
        if a not in self.parent:
            self.parent[a] = a
            return a

        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return

        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = self.parent[pa]
            self.rank[pa] = self.rank[pa] + self.rank[pb]
        else:
            self.parent[pa] = self.parent[pb]
            self.rank[pb] = self.rank[pa] + self.rank[pb]







class Solution2:
    # Coloring technique
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        arr = [-1 for _ in range(n + 1)]
        map = defaultdict(set)

        for a, b in dislikes:
            map[a].add(b)
            map[b].add(a)

        for i in range(1, n + 1):
            q = deque([i])
            while q:
                node = q.popleft()
                if arr[node] == -1:
                    arr[node] = 0
                for adj in map[node]:
                    if arr[adj] == arr[node]:
                        return False
                    if arr[adj] == -1:
                        arr[adj] = abs(arr[node] - 1)
                        q.append(adj)

        return True
