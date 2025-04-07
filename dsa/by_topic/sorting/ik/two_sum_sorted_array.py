# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# using binary search
# Time complexity O(nlogn)
# Space complexity O(1)
def pair_sum_sorted_array(numbers, target):
    def binary_search(start, end, tgt):
        if start > end:
            return -1
        mid = start + (end - start) // 2
        if tgt > numbers[mid]:
            return binary_search(mid + 1, end, tgt)
        elif tgt < numbers[mid]:
            return binary_search(start, mid - 1, tgt)
        else:
            return mid

    for idx, num in enumerate(numbers):
        tgt = target - numbers[idx]
        tgt_index = binary_search(idx + 1, len(numbers) - 1, tgt)
        if tgt_index != -1:
            return [idx, tgt_index]

    return [-1, -1]


# using 2 pointer approach
# Time complexity O(n)
# Space complexity O(1)
def pair_sum_sorted_array_two_pointer(numbers, target):
    p1 = 0
    p2 = len(numbers) - 1
    while p2 > p1:
        sum = numbers[p1] + numbers[p2]
        if sum > target:
            p2 -= 1
        elif sum < target:
            p1 += 1
        else:
            return [p1, p2]
    return [-1, -1]
