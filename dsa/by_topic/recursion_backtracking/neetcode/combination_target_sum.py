"""
https://neetcode.io/problems/combination-target-sum
"""

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def helper(slate, total_sum, index):
            if total_sum == target:
                output.append(slate[:])
                return
            if total_sum > target:
                return

            for idx in range(index,len(nums)):
                num =nums[idx]
                slate.append(num)
                helper(slate, total_sum + num, idx)
                slate.pop()

        helper([],0,0)
        return output