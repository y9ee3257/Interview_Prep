# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
            [1,2,3,4,5,6].  [4,5,6]
                 i
                 k
                            j

            3 - 6 and replace k with higher number

            [2,2]. [1]
        i.   k
                    j
        """

        i = m - 1
        j = n - 1
        k = len(nums1) - 1

        while j >= 0:
            if i < 0 or nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        return nums1






