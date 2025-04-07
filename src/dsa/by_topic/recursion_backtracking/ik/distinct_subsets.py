"""
Subsets With Duplicate Characters
Given a string that might contain duplicate characters, find all the possible distinct subsets of that string.

Example One
{
"s": "aab"
}
Output:

["", "a", "aa", "aab", "ab", "b"]
Example Two
{
"s": "dc"
}
Output:

["", "c", "cd", "d"]
Notes
All the subset strings should be individually sorted.
The order of the output strings does not matter.
Constraints:

1 <= length of the string <= 15
String consists of lowercase English letters
"""

def get_distinct_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """

    output = set()
    sorted_s = sorted(s)

    def helper(slate ,index):
        output.add("".join(slate))
        if index == len(s):
            return
        # include current char
        slate.append(sorted_s[index])
        helper(slate ,index +1)
        slate.pop()
        # exclude current char
        helper(slate ,index +1)

    helper([] ,0)
    return list(output)