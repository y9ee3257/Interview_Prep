"""
https://leetcode.com/problems/similar-string-groups/
"""

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        uf = UnionFind()

        for i in range(len(strs)):
            for j in range(i,len(strs)):
                similar = self.is_similar(strs[i],strs[j])
                if similar:
                    uf.union(strs[i],strs[j])

        output = set()
        for string in strs:
            parent = uf.find(string)
            output.add(parent)

        return len(output)


    def is_similar(self,a,b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count+=1
        # similar if no swaps or 1 swap (2 chars change)
        return count == 0 or count == 2


class UnionFind:

    def __init__(self):
        self.parent = {}
        self.rank = defaultdict(lambda:1)

    def find(self,a):
        if a not in self.parent:
            self.parent[a] = a

        if a != self.parent[a]:
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


