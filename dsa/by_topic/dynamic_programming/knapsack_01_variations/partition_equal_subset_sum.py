"""
https://leetcode.com/problems/partition-equal-subset-sum/description/
"""


class PartitionSumRecursive:
    """
    This is same as subset sum equals target problem. 
    Check if any subset has a sum equal to half of the total sum
    """

    def solution(self, nums):
        total = sum(nums)
        # sum of two numsbers will always be even.
        if total % 2 != 0:
            return False
        self.nums, self.target = nums, total // 2
        return self.helper(0, 0)

    def helper(self, total, index):
        if total == self.target:
            return True
        if index == len(self.nums):
            return False
        include = self.helper(total + self.nums[index], index + 1)
        exclude = self.helper(total, index + 1)
        return include or exclude


class PartitionSumRecursiveMemoization:

    def solution(self, nums):
        total = sum(nums)
        # sum of two numsbers will always be even.
        if total % 2 != 0:
            return False
        target = total // 2

        # It is important to initialize with -1 instead of False,
        # to avoid confusion b/w actual result being False vs no processed
        self.memo = [[-1 for _ in range(target)] for _ in range(len(nums))]
        self.nums, self.target = nums, target
        return self.helper(0, 0)

    def helper(self, total, index):
        if total == self.target:
            return True
        if index == len(self.nums) or total > self.target:
            return False

        if self.memo[index][total] != -1:
            return self.memo[index][total]

        include = self.helper(total + self.nums[index], index + 1)
        exclude = self.helper(total, index + 1)
        res = include or exclude
        self.memo[index][total] = res
        return res


class PartitionSumIterative:
    def solution(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        output = [[-1 for _ in range(target + 1)] for _ in range(len(nums))]

        for index in range(len(nums)):
            for target_sum in range(target + 1):
                if target_sum == 0:
                    output[index][target_sum] = False
                elif index == 0:
                    output[index][target_sum] = target_sum == nums[index]
                else:
                    include = output[index - 1][target_sum - nums[index]] if nums[index] < target_sum else False
                    exclude = output[index - 1][target_sum]
                    output[index][target_sum] = include or exclude

        return output[len(nums) - 1][target]


class PartitionSumRecursive2:
    """
    Two array approach is little tricky when implementing memoization and bottom up approach, 
    because there will be 3 variables (sum1, sum2, index) and the result itself (True/False)
    """

    def solution(self, nums):
        self.arr = list(nums)
        return self.helper(0, 0, 0)

    def helper(self, total1, total2, index):
        if index == len(self.arr):
            return total1 == total2

        res1 = self.helper(total1 + self.arr[index], total2, index + 1)
        res2 = self.helper(total1, total2 + self.arr[index], index + 1)

        return res1 or res2
