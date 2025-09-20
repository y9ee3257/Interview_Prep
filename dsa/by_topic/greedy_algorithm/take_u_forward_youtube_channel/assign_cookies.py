"""
https://leetcode.com/problems/assign-cookies/
"""


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        l, r = 0, 0

        while r < len(g) and l < len(s):
            if s[l] >= g[r]:
                r += 1
            l += 1

        return r
