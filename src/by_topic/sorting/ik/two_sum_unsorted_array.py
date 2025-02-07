# https://leetcode.com/problems/two-sum/description/

# using a dictionary
# time complexity O(n)
# space complexity O(n)
def two_sum(numbers, target):
    dict = {}
    for idx ,num in enumerate(numbers):
        tgt = target - num
        if tgt in dict:
            return [idx, dict[tgt]]
        dict[num] = idx
    return [-1 ,-1]
