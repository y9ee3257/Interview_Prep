# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        """
            [2,1,1,-1,3,-3,2] k = 1

            calculate the total sum from left, one element at a time

            [2]
            [2,1]
            [2,1,1]
            ...

            for every total, save the value in a dict and increment the number of occurances
            if we want to know there is a subset who's sum is equal to k
            assume x+y=total, where x is the subset whose sum is equal to k

            y = total - x

            so, just check if there exists a prefix sum who's sum is equal to (total-x) from the dict.
            If exists, check how many times it exists. That's how many ways you can form a subset with sum=k in the given subseet


            example: for subset [2,1,1] and k =1
            if there exists a subset with sum=k, assume the subset to be x
            x+y=total --> 1+y=4 --> y =3
            check if there exists a prefix sum who's value is 3
            [2,1] + [1] --> [1] is equal to sum k

        """

        prefix_sum = {0: 1}
        total = 0
        result = 0
        for i in range(len(nums)):
            total += nums[i]
            if total - k in prefix_sum:
                result += prefix_sum[total - k]

            if total in prefix_sum:
                prefix_sum[total] += 1
            else:
                prefix_sum[total] = 1

        return result


