"""
https://leetcode.com/problems/3sum/description/
"""


class Solution:
    def searchTriplets(self, arr):
        triplets = []

        arr.sort()

        #  [-3, 0, 1, 2, -1, 1, -2]
        #  [-3, -3, -2, -1, 0, 1, 1, 1, 1, 2, 2]
        i = 0
        while i < len(arr):
            l, r = i + 1, len(arr) - 1

            while l < r:
                total = arr[i] + arr[l] + arr[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    triplets.append([arr[i], arr[l], arr[r]])
                    l += 1
                    while 0 < l < len(arr) and arr[l] == arr[l - 1]:
                        l += 1
            i += 1
            while 0 < i < len(arr) and arr[i] == arr[i - 1]:
                i += 1
        return triplets
