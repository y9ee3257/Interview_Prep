"""
https://leetcode.com/problems/single-element-in-a-sorted-array/
"""


class Solution:
    def singleNonDuplicate(self, nums):
        output = []
        def binary_search(start, end):
            if start > end or not (0 <= start < len(nums) and 0 <= end < len(nums)):
                return

            mid = start + (end - start) // 2

            mid_val = nums[mid]
            mid_left = nums[mid - 1] if mid - 1 >= 0 else None
            mid_right = nums[mid + 1] if mid + 1 < len(nums) else None

            if mid_val != mid_left and mid_val != mid_right:
                output.append(mid_val)

            if (mid % 2 == 0 and mid_val == mid_right) or (mid % 2 != 0 and mid_val == mid_left):
                binary_search(mid + 1, end)
            else:
                binary_search(start, mid - 1)

        binary_search(0, len(nums) - 1)

        return output[0]
