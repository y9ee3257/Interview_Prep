# You're given an array of integers and a target Return the min sum of the lengths of two non-overlapping subarrays such that the sum of the elements
# in each subarray equals target Return -1 if not possible Example: Input: arr = [3,2,2,4,3], target = 3 Output: 2
#   0. 1  2  3. 4
# [1, 2, 2, 4, 3]
#              lr
# Time = O(n)
# Space = O(1)
def min_sum(arr, target):
    l,r = 0,0
    arr1_len = None # 1
    arr2_len = None

    total = 0 # 4
    while r<len(arr): # 3
        val = arr[r] # 3
        total += val # 4+3=7

        # if at any point total is greater than target, reduce the window by moving l and reducing the total
        while l<=r and total > target:
            total -= arr[l]
            l+=1

        if total == target: # true
            length = r-l+1 # 1
            # assigning length to the least value
            if not arr1_len:
                arr1_len = length
            elif not arr2_len:
                arr2_len = length
            elif arr1_len > arr2_len:  # arr1 = 2 , arr2 = 3     newlen = 2
                arr1_len = min(arr1_len, length)
            else:
                arr2_len = min(arr2_len, length)

            # incrementing l,r to the next value, to avoid overlapping
            l,r = r+1, r+1 # 1,1
            total = 0
            continue

        r+=1

    if not arr1_len or not arr2_len:
        return -1

    return arr1_len+arr2_len

print(min_sum([1, 2, 1, 2],3))




