# https://www.educative.io/courses/grokking-coding-interview-patterns-python/remove-all-adjacent-duplicates-in-string
# You are given a string consisting of lowercase English letters.
# Repeatedly remove adjacent duplicate letters, one pair at a time.
# Both members of a pair of adjacent duplicate letters need to be removed.

# Input
# "aannkwwwkkkwna"
# Output
# "kwkwna"
#
# Input
# "abbddaccaaabcd"
# Output
# "abcd"
#
# Input:
# "aabbccdd"
# Output:
# ""

from collections import deque
def remove_duplicates(string):
    stack = deque()
    for char in string:
        if len(stack)==0 or stack[-1]!=char:
            stack.append(char)
        else:
            stack.pop()
    return "".join(stack)
