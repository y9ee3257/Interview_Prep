"""
https://neetcode.io/problems/longest-repeating-substring-with-replacement
"""

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = {}
        max_freq = 0
        p1,p2, max_len= 0,0,0

        while p2 < len(s):
            freq[s[p2]] = freq.get(s[p2],0) + 1
            max_freq = max(max_freq,freq[s[p2]])

            while (p2-p1+1) - max_freq > k:
                freq[s[p1]]-=1
                p1+=1
            max_len = max(max_len,p2-p1+1)
            p2+=1

        return max_len







