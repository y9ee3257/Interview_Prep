"""
https://neetcode.io/problems/subsets-ii
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #constraints - There can be duplicates
        #each element can be chosen atmost once
        #order of numbrs in each combo can be in any order

        #base condition - sum == target, [1,2,5 ] -- already existed in o/p
        sorted_candidates = sorted(nums)
        output = []
        def helper(slate, idx):
            if idx >= len(sorted_candidates):
                output.append(slate[:])
                return
            #inclde case
            slate.append(sorted_candidates[idx])
            curr = sorted_candidates[idx]
            helper(slate,idx+1)
            slate.pop()
            #exclude
            while idx < len(sorted_candidates) and sorted_candidates[idx] == curr :
                idx+=1
            helper(slate,idx)

        helper([],0)
        return output