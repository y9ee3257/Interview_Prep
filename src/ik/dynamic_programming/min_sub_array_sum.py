# Given an array containing n integers. The problem is to find the sum of the elements of the contiguous subarray having the smallest(minimum) sum.
#
# Examples:
#
# Input : arr[] = {3, -4, 2, -3, -1, 7, -5}
# Output : -6
# Subarray is {-4, 2, -3, -1} = -6
# Input : arr = {2, 6, 8, 1, 4}
# Output : 1
import math
def min_subarray_len(nums):
    storage = [0] * len(nums)
    storage[0] = nums[0]
    min_sofar = nums[0]
    for i in range(1, len(nums)):
        storage[i] = min(storage[i-1] + nums[i] , nums[i])
        min_sofar = min(min_sofar,storage[i])

    return min_sofar





print(min_subarray_len( [2, 6, 8, 1, 4]))