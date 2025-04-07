"""
Given a sorted array of integers with duplicates, count the number of unique values.

Input:
{4,5,8}

444588

444444444444444444555555555555555555555555555557778888888888888888888888888888999999999999999

klog(n)

Output:
3

(Explanation: there are 3 distinct values: 4, 5, 8)

Assume that the number of unique elements, K, is much less than the size of the array, N
e.g. K = O(log N)
     K = O(sqrt (sqrt(N)))
"""

from bisect import bisect_right

def find_unique2(arr):
    index =0
    count = 0
    while index < len(arr):
        val = arr[index]
        count+=1
        index = bisect_right(arr,val,index,len(arr))
    return count