"""
https://neetcode.io/problems/is-palindrome
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        .,
        i,j
        """
        if len(s)==1:
            return True

        new_str = s.replace(" ","").lower()
        i,j = 0, len(new_str)-1

        while i<=j:
            if not new_str[i].isalpha() and not new_str[i].isnumeric():
                i+=1
                continue
            if not new_str[j].isalpha() and not new_str[j].isnumeric():
                j-=1
                continue

            if new_str[i] != new_str[j]:
                return False
            i,j = i+1, j-1

        return True



