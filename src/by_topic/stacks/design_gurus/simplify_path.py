"""
Problem Statement
Given an absolute file path in a Unix-style file system, simplify it by converting ".." to the previous directory and removing any "." or multiple slashes. The resulting string should represent the shortest absolute path.

Examples:
1.
   Input: "/a//b////c/d//././/.."
   Output: "/a/b/c"

2.
   Input: "/../"
   Output: "/"

3.
   Input: "/home//foo/"
   Output: "/home/foo"
Constraints:

1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.

"""


class Solution:
    def simplifyPath(self, path):
        new_path = path.split("/")
        stack = []
        for substring in new_path:
            if substring == "..":
                if stack:
                    stack.pop()
            elif substring and substring != ".":
                stack.append(substring)

        return "/" + "/".join(stack)
