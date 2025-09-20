"""
https://leetcode.com/problems/find-the-town-judge/description/
"""

from collections import defaultdict

class Solution:
    def findTownJudge(self, N: int, trust: list[list[int]]) -> int:

        if N==1:
            return 1

        trust_map = defaultdict(set)
        trusted_map = defaultdict(set)
        for t in trust:
            trust_map[t[1]].add(t[0])
            trusted_map[t[0]].add(t[1])

        for i in range(1,N+1):
            if i not in trusted_map and i in trust_map and len(trust_map[i])==N-1:
                return i

        return -1


