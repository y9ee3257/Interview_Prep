# https://leetcode.com/problems/longest-substring-without-repeating-characters/editorial/


"""
Using two pointer approach
Time O(n)
Space O(n)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, freq_map, max_len = 0, {}, 0

        for right in range(0, len(s)):
            cur_char = s[right]

            while cur_char in freq_map:
                left_char = s[left]
                del freq_map[left_char]
                left += 1

            freq_map[cur_char] = 1
            max_len = max(max_len, len(freq_map))

        return max_len



