"""
https://leetcode.com/problems/sort-colors/description/
"""


class Solution:
    def sort(self, arr):

        print(arr)
        l, r = 0, len(arr) - 1

        while l < r:
            if arr[l] == 0:
                l += 1
                continue

            if arr[r] != 0:
                r -= 1
                continue

            arr[l], arr[r] = arr[r], arr[l]

        r = len(arr) - 1

        while l < r:
            if arr[l] == 1:
                l += 1
                continue

            if arr[r] != 1:
                r -= 1
                continue

            arr[l], arr[r] = arr[r], arr[l]

        return arr



