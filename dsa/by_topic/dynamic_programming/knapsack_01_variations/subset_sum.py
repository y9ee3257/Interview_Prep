"""
https://www.geeksforgeeks.org/dsa/subset-sum-problem-dp-25/

Subset Sum Problem
Last Updated : 23 Jul, 2025
Given an array arr[] of non-negative integers and a value sum, the task is to check if there is a subset of the given array whose sum is equal to the given sum.

Examples:

Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 9
Output: True
Explanation: There is a subset (4, 5) with sum 9.

Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 30
Output: False
Explanation: There is no subset that add up to 30.
"""


class SubsetSumRecursive:
    def isSubsetSum(self, arr, sum):
        self.arr, self.sum = arr, sum
        self.memo = [[-1 for _ in range(sum + 1)] for _ in range(len(arr))]
        return self.helper(0, 0)

    def helper(self, total, index):
        if total == self.sum:
            return True

        if total > self.sum or index == len(self.arr):
            return False

        if self.memo[index][total] != -1:
            return self.memo[index][total]

        include = self.helper(total + self.arr[index], index + 1)
        exclude = self.helper(total, index + 1)

        self.memo[index][total] = include or exclude

        return include or exclude


class SubsetSumIterative:
    def isSubsetSum(self, arr, sum):
        n = len(arr)
        output = [[False for _ in range(sum + 1)] for _ in range(n)]

        for index in range(n):
            for target in range(sum + 1):
                if target == 0:
                    output[index][target] = True
                elif index == 0:
                    output[index][target] = arr[index] == target
                else:
                    include = False
                    if arr[index] <= target:
                        include = output[index - 1][target - arr[index]]
                    exclude = output[index - 1][target]
                    output[index][target] = include or exclude
        return output[n - 1][sum]


instance = SubsetSumRecursive()
print(instance.isSubsetSum([3, 34, 4, 12, 5, 2], 9))

instance = SubsetSumIterative()
print(instance.isSubsetSum([3, 34, 4, 12, 5, 2], 30))
