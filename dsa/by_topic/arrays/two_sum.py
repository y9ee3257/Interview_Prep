class Solution:
    def threeSum(self, nums):

        nums.sort()
        output = []
        for idx, num in enumerate(nums):
            result = self.two_sum(nums, idx + 1, -num)
            if result:
                for res in result:
                    output.append(res)
        return output

    def two_sum(self, nums, start, target):
        i, j = start, len(nums) - 1
        output_inner = []
        while i < j:
            sum_1 = nums[i] + nums[j]
            if sum_1 == target:
                output_inner.append([nums[i], nums[j], -target])
                i, j = i + 1, j - 1
            elif sum_1 > target:
                j -= 1
            elif sum_1 < target:
                i += 1
        print("two sum output", list(output_inner))
        return output_inner



test = Solution()
test.threeSum([-1,0,1,2,-1,-4])