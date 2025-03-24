# https://neetcode.io/problems/trapping-rain-water

class Solution:
    def trap(self, height) -> int:

        prefix_arr = []
        suffix_arr = []
        for idx in range(len(height)):
            prefix_hgt = height[idx]
            suffix_hgt = height[-idx - 1]
            prefix_arr.append(max(prefix_hgt, prefix_arr[-1] if prefix_arr else 0))
            suffix_arr.append(max(suffix_hgt, suffix_arr[-1] if suffix_arr else 0))
        suffix_arr.reverse()
        trapped_wtr = 0

        for idx, hgt in enumerate(height):
            trapped_wtr += max(min(prefix_arr[idx], suffix_arr[idx]) - hgt, 0)

        return trapped_wtr
