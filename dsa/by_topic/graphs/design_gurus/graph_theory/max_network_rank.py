
"""
https://leetcode.com/problems/maximal-network-rank/
"""

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        map = defaultdict(set)

        for road in roads:
            map[road[0]].add(road[1])
            map[road[1]].add(road[0])

        visited = set()

        max_rank = 0
        for i in range(n):
            for j in range(i+1,n):
                rank1= len(map[i])
                rank2= len(map[j])
                if j in map[i]:
                    rank1-=1
                max_rank = max(max_rank, rank1+rank2)
        return max_rank


