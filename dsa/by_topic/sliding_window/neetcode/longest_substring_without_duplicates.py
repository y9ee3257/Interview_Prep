"""
https://neetcode.io/problems/longest-substring-without-duplicates
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0

        p1, p2, max_len, char_set = 0, 0,0, set()

        while p2 < len(s):
            while s[p2] in char_set:
                char_set.remove(s[p1])
                p1+=1
            max_len  = max(max_len, p2-p1+1)
            char_set.add(s[p2])
            p2+=1
        return max_len
