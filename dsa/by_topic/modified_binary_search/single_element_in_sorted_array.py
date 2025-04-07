# https://www.educative.io/courses/grokking-coding-interview-patterns-python/single-element-in-a-sorted-array
#
# You are given a sorted array of integers, nums, where all integers appear twice except for one.
# Your task is to find and return the single integer that appears only once.
#
# The solution should have a time complexity of O(logn) or better and a space complexity of O(1).

# Input
# [1, 1, 2, 2, 3, 3, 4, 4, 5, 8, 8]
# Output
# 5

# Input
# [0, 0, 1, 1, 2, 2, 4, 8, 8, 16, 16, 32, 32]
# Output
# 4

def single_non_duplicate(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if mid < len(arr) - 1 and arr[mid + 1] == arr[mid]:
            mid = mid + 1
        elif mid > 0 and arr[mid - 1] == arr[mid]:
            mid = mid
        else:
            return arr[mid]

        if (mid - left + 1) % 2 == 0:
            left = mid + 1
        else:
            right = mid - 1
    return -1
