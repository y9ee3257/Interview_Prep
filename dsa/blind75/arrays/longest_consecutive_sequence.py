"""
https://neetcode.io/problems/longest-consecutive-sequence
"""



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = {}

        for num in nums:
            map[num] = False

        max_count = 0
        for num in nums:
            count = 0
            current = num
            # check forward
            while current in map and map[current]==False:
                count+=1
                map[current] = True
                current+=1

            # check backward
            current = num-1
            while current in map and map[current]==False:
                count+=1
                map[current] = True
                current-=1

            max_count = max(max_count,count)

        return max_count




