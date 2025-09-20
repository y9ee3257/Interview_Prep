"""
https://leetcode.com/problems/accounts-merge/
"""

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        map = {}
        for account in accounts:
            account_name = account[0]
            main_email = account[1]
            for i in range(1,len(account)):
                curr_email = account[i]
                map[curr_email] = account_name
                uf.union(main_email, curr_email)

        output_map = defaultdict(list)
        for email in map.keys():
            parent = uf.find(email)
            account_name = map[parent]
            output_map[parent].append(email)

        for key in output_map.keys():
            output_map[key].sort()
            output_map[key] = [map[key]]+output_map[key]

        return list(output_map.values())



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
