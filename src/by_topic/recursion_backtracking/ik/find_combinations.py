# N Choose K Combinations
# Given two integers n and k, find all the possible unique combinations of k numbers in range 1 to n.
#
# Example One
# {
#     "n": 5,
#     "k": 2
# }
# Output:
#
# [
#     [1, 2],
#     [1, 3],
#     [1, 4],
#     [1, 5],
#     [2, 3],
#     [2, 4],
#     [2, 5],
#     [3, 4],
#     [3, 5],
#     [4, 5]
# ]
# Example Two
# {
#     "n": 6,
#     "k": 6
# }
# Output:
#
# [
#     [1, 2, 3, 4, 5, 6]
# ]
# Notes
# The answer can be returned in any order.
#
# Constraints:
#
# 1 <= n <= 20
# 1 <= k <= n

output = []


def find_combinations(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    helper(n, k, 1, [])
    return output


def helper(n, k, index, slate):
    if len(slate) == k:
        output.append(slate[:])
        return
    if index > n:
        return

    slate.append(index)
    helper(n, k, index + 1, slate)
    slate.pop()

    helper(n, k, index + 1, slate)
