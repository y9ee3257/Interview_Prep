"""
https://neetcode.io/problems/permutations
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        output = []

        def helper(slate, remaining):
            if len(slate) == len(nums):
                output.append(slate[:])
                return

            new_set = remaining.copy()
            for num in remaining:
                slate.append(num)
                new_set.remove(num)
                helper(slate, new_set)
                new_set.add(num)
                slate.pop()

        helper([],set(nums))
        return output
