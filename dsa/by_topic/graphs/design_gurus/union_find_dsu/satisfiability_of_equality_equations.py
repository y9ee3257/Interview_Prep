"""
https://leetcode.com/problems/satisfiability-of-equality-equations/
"""

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()

        for eq in equations:
            if eq[1] == "=":
                uf.union(eq[0],eq[3])

        for eq in equations:
            if eq[1] == "!" and uf.find(eq[0]) == uf.find(eq[3]):
                return False
        return True

class UnionFind:

    def __init__(self):
        self.parent = {}
        self.rank = defaultdict(lambda:1)

    def find(self,a):
        if a not in self.parent:
            self.parent[a] = a
            return a

        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self,a,b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return

        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = self.parent[pa]
            self.rank[pa] = self.rank[pa]+self.rank[pb]
        else:
            self.parent[pa] = self.parent[pb]
            self.rank[pb] = self.rank[pa]+self.rank[pb]





