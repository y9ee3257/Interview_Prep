# https://www.educative.io/courses/grokking-coding-interview-patterns-python/find-k-closest-elements

# You are given a sorted array of integers, nums, and two integers, target and k.
# Your task is to return k number of integers that are close to the target value, target.
# The integers in the output array should be in a sorted order.
#
# An integer, nums[i], is considered to be closer to target,
# as compared to nums[j] when |nums[i] - target|< |nums[j] - target|.
# However, when |nums[i] - target|==|nums[j] - target|, the smaller of the two values is selected.
#
# Input
# [1, 2, 3, 4, 5] , 4 , 3
# Output
# [1, 2, 3, 4]
#
# Input
# [-29, -11, -3, 0, 5, 10, 50, 63, 198] , 6 , 8
# Output
# [-29, -11, -3, 0, 5, 10]

def find_closest_elements(nums, k, target):
    left = 0
    right = len(nums) - 1
    closest = float("inf")
    closest_index = 0
    while (left <= right):
        mid = (left + right) // 2
        if abs(nums[mid] - target) < abs(closest - target):
            closest = nums[mid]
            closest_index = mid
        if target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    left = closest_index
    right = closest_index
    while left >= 0 and right < len(nums) and right - left < k:
        if abs(nums[left] - target) <= abs(nums[right] - target):
            left -= 1
        else:
            right += 1

    if left < 0:
        return nums[0:k]
    elif right >= len(nums):
        return nums[-k:]
    else:
        return nums[left:right]
