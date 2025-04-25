"""
https://neetcode.io/problems/subsets
"""

class Solution:
    def subsets(self, nums):

        """
                                            []
                                    [],0    /\
                                         [1]  []
                                        /\
                                   [1,2]
                                     /\
                             [1,2,3]  [1,2]


       output =[[1,2,3],[1,2]]
        """

        output = []

        def helper(slate, index):  # [1,2], 3
            if index == len(nums):
                output.append(slate[:])
                return
            # [1,2,3]
            element = nums[index] # 2
            # include element at index
            slate.append(element) # [1,2,3]
            helper(slate, index+1) # [1,2,3],3
            slate.pop()          # [1,2]

            # exclude element at index
            helper(slate, index+1) # [1,2], 3

        helper([],0)

        return output
