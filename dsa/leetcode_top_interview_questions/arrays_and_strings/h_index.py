# https://leetcode.com/problems/h-index/description/
"""
learn count sort
sorting can be done in O(n) if the range is low
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:

        n = len(citations)
        new_arr = self.count_sort(citations, n)

        for i, val in enumerate(new_arr):
            if val >= n - i:
                return n - i

        return 0

    def count_sort(self, nums, n):
        freq_arr = [0] * (n + 1)

        # trim all the values greater than n, since it does not make any difference. It will help in counting sort
        for val in nums:
            freq_arr[min(n, val)] += 1

        # array will look like
        # [3,0,6,1,5] --> [3,0,5,1,5] --> [1,1,0,1,0,2] (0's=1, 1's=1,2's=0,3's=1,4's=0,5's=2)
        # expand this [1,1,0,1,0,2] to [0,1,3,5,5]
        result = []
        for i, freq in enumerate(freq_arr):
            while freq > 0:
                result.append(i)
                freq -= 1

        return result