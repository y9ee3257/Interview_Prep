"""
https://leetcode.com/problems/valid-palindrome-ii/
"""


class Solution:
    def isPalindromePossible(self, s: str) -> bool:

        l, r, count = 0, len(s) - 1, 0

        while l <= r:
            if s[l] == s[r]:
                l, r = l + 1, r - 1
            else:
                count += 1
                if count > 1:
                    return False
                if s[l + 1] == s[r]:
                    l += 1
                else:
                    r -= 1

        return True


