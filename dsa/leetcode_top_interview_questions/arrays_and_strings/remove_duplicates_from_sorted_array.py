# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # No swap, i keeps track of next index where the element can be placed
        #          j finds the next unique element and replaces the value in i

        # 0 1 2 3 4 2 2 3 3 4
        #         i
        #                     j

        # 1 2 3 4 5
        #     i
        #     j

        l, r = 0, 0
        while r < len(nums):
            if r == 0 or nums[r - 1] != nums[r]:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l

