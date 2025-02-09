"""
Give a string s, convert it into a valid string. A string is considered valid if it does not have any two adjacent duplicate characters.

To make a string valid, we will perform a duplicate removal process. A duplicate removal consists of choosing two adjacent and equal letters and removing them. We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

Examples
Example 1

Input: "abbaca"
Expected Output: "ca"
Description: We remove 'b' from "abbaca" to get "aaca", then remove 'a' from "aaca" to get "ca"
Example 2

Input: "azxxzy"
Expected Output: "ay"
Description: We remove 'x' from "azxxzy" to get "azzy", then remove 'z' from "azzy" to get "ay"
Example 3

Input: "abba"
Expected Output: ""
Description: We remove 'b' from "abba" to get "aa", then remove 'a' from "aa" to get an empty string
Constraints:

1 <= str.length <= 105
str consists of lowercase English letters.
"""


class Solution:
    def removeDuplicates(self, s):
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
