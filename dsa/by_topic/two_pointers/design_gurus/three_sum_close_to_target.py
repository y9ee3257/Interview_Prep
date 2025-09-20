"""
https://leetcode.com/problems/3sum-closest/
"""

import math


class Solution:
    def searchTriplet(self, arr, target_sum):

        res = []
        triplet_sum = math.inf
        arr.sort()

        for i in range(len(arr)):
            l, r = i + 1, len(arr) - 1

            while l < r and r < len(arr):
                total = arr[l] + arr[r] + arr[i]
                diff = total - target_sum
                res_diff = triplet_sum - target_sum
                if total > target_sum:
                    r -= 1
                elif total < target_sum:
                    l += 1
                else:
                    l, r = l + 1, r - 1

                print(diff, triplet_sum)
                if abs(diff) < abs(res_diff) or (abs(diff) == abs(res_diff) and total < target_sum):
                    res = [arr[l], arr[r], arr[i]]
                    triplet_sum = total

        return triplet_sum
