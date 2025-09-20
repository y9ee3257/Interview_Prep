
"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
"""

class Solution:
    def search(self, arr, target_sum):

        l ,r = 0, len(arr ) -1

        while l < r:
            if arr[r ] +arr[l] == target_sum:
                return [r ,l]
            elif arr[r ] +arr[l] < target_sum: l+=1
            else:
                r-=1

        return [-1,-1]

