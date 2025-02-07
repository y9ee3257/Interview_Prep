# Generate All Subsets Of A Set
# Generate ALL possible subsets of a given set. The set is given in the form of a string s containing distinct lowercase characters 'a' - 'z'.
#
# Example
# {
#     "s": "xy"
# }
# Output:
#
# ["", "x", "y", "xy"]
# Notes
# Any set is a subset of itself.
# Empty set is a subset of any set.
# Output contains ALL possible subsets of given string.
# Order of strings in the output does not matter. E.g. s = "a", arrays ["", "a"] and ["a", ""] both will be accepted.
# Order of characters in any subset must be same as in the input string. For s = "xy", array ["", "x", "y", "xy"] will be accepted, but ["", "x", "y", "yx"] will not be accepted.
# Constraints:
#
# 0 <= length of s <= 19
# s only contains distinct lowercase English letters.


output = []


def helper(input_arr, idx, slate):
    if idx == len(input_arr):
        output.append("".join(slate))
        return

    # exclude the element
    helper(input_arr, idx + 1, slate)

    # include the element
    slate.append(input_arr[idx])
    helper(input_arr, idx + 1, slate)
    slate.pop()


def generate_all_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    helper(list(s), 0, [])
    return output

