"""
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
"""
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()
        rowmap = defaultdict(list)
        colmap = defaultdict(list)

        for coord in stones:
            coordinateStr = str(coord[0])+"-"+str(coord[1])
            rowmap[coord[0]].append(coordinateStr)
            colmap[coord[1]].append(coordinateStr)

        for row in rowmap.keys():
            coordinatesList = rowmap[row]
            if len(coordinatesList) > 1:
                parent = coordinatesList[0]
                for coord in coordinatesList:
                    uf.union(coord,parent)

        for col in colmap.keys():
            coordinatesList = colmap[col]
            if len(coordinatesList) > 1:
                parent = coordinatesList[0]
                for coord in coordinatesList:
                    uf.union(coord,parent)

        uniqueParents = set()
        for coord in stones:
            coordinateStr = str(coord[0])+"-"+str(coord[1])
            parent = uf.find(coordinateStr)
            uniqueParents.add(parent)

        return len(stones) - len(uniqueParents)


class UnionFind:

    def __init__(self):
        self.parent = {}
        self.rank = defaultdict(lambda:1)

    def find(self,a):
        if a not in self.parent:
            self.parent[a] = a

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
