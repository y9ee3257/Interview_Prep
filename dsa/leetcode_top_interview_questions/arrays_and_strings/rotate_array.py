# https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        self.reverse(0, n - k - 1, nums)
        self.reverse(n - k, n - 1, nums)
        self.reverse(0, n - 1, nums)

    def reverse(self, start, end, nums):
        while (start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


