"""
https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
"""
from typing import List


class Tabulation:
    def minimumDifference(self, nums: List[int]) -> int:
        total = sum(nums)
        target = total // 2
        size = len(nums)

        output = [[False for _ in range(target + 1)] for _ in range(size)]

        for index in range(size):
            for capacity in range(target + 1):
                if capacity == 0:
                    output[index][0] = True
                elif index == 0:
                    output[0][capacity] = nums[index] == capacity
                else:
                    include = False
                    if capacity - nums[index] >= 0:
                        include = output[index - 1][capacity - nums[index]]
                    exclude = output[index - 1][capacity]
                    output[index][capacity] = include or exclude

        for i in range(target, -1, -1):
            if output[size - 1][i]:
                return total - (2 * i)

        return 0
