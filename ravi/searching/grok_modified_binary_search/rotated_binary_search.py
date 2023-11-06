#https://www.educative.io/courses/grokking-coding-interview-patterns-python/search-in-rotated-sorted-array
#
# Given a sorted integer array, nums, and an integer value, target, the array is rotated by some arbitrary number.
# Search and return the index of target in this array. If the target does not exist, return -1.
#
# An original sorted array before rotation is given below:
#
# After rotating this array 6 times, it changes to:
#
# Constraints
#
# All values in nums are unique.
# The values in nums are sorted in ascending order.
# The array may have been rotated by some arbitrary number.


def rotated_binary_search(array, target):
    return rotated_binary_search_rec(array, target, 0, len(array) - 1)


def rotated_binary_search_rec(array, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if target == array[mid]:
        return mid
    elif target < array[start] and target <= array[end]:
        return rotated_binary_search_rec(array, target, mid + 1, end)
    else:
        return rotated_binary_search_rec(array, target, start, mid - 1)


print(rotated_binary_search([4, 5, 6, 1, 2, 3], 1))
print(rotated_binary_search([4, 5, 6, 1, 2, 3], 2))
print(rotated_binary_search([4, 5, 6, 1, 2, 3], 3))
print(rotated_binary_search([4, 5, 6, 1, 2, 3], 4))
print(rotated_binary_search([4, 5, 6, 1, 2, 3], 5))
print(rotated_binary_search([4, 5, 6, 1, 2, 3], 6))
