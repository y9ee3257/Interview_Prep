# Permute Array Of Unique Integers
# Given an array of unique numbers, return in any order all its permutations.
#
# Example
# {
#     "arr": [1, 2, 3]
# }
# Output:
#
# [
#     [1, 2, 3],
#     [1, 3, 2],
#     [2, 1, 3],
#     [2, 3, 1],
#     [3, 2, 1],
#     [3, 1, 2]
# ]
# Notes
# Constraints:
#
# 1 <= size of the input array <= 9
# 0 <= any array element <= 99


output = []
def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    helper(arr, [])
    return output


def helper(remaining, slate):
    if len(remaining) == 0:
        output.append(slate[:])
        return

    for idx, value in enumerate(remaining):
        new_rem = remaining[:idx] + remaining[idx + 1:]
        slate.append(value)
        helper(new_rem, slate)
        slate.pop()
