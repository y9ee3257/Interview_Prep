import math


def merge(arr1, arr2):
    """
    Uses merging in place
    Time Complexity O(n+m)
    Space Complexity O(1)

    [1,3,5]  [4,12,13]
    [1,3,4,5,12,13]  [4,12,13]
       p1p3
    """
    p1, p2= len(arr1)-1, len(arr2)-1
    for i in range(len(arr2)):
        arr1.append(0)
    p3 = len(arr1)-1

    while p1 >=0 and p2 >=0:
        if arr1[p1] <= arr2[p2]:
            arr1[p3] = arr2[p2]
            p2, p3 = p2-1, p3-1
        else:
            arr1[p3] = arr1[p1]
            p1, p3 = p1-1, p3-1

    while p2 >=0:
        arr1[p3] = arr2[p2]
        p2, p3 = p2 - 1, p3 - 1

    return arr1



def merge_sorted_arrays(arr1, arr2):
    """
     [1 2 3 4 5]
            p1
                  = [1,2,3,4,]
            p3
     [3 4 5 6 7]
       p2
    """

    final_arr = []
    p1 = 0
    p2 = 0
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            final_arr.append(arr1[p1])
            p1 += 1
        else:
            final_arr.append(arr2[p2])
            p2 += 1

    while p1 < len(arr1):
        final_arr.append(arr1[p1])
        p1 += 1
    while p2 < len(arr2):
        final_arr.append(arr2[p2])
        p2 += 1

    return final_arr


def merge_sort(arr, start, end):
    if len(arr)==0:
        return []
    if start == end:
        return [arr[start]]

    mid = start + (end-start)//2
    m1 = merge_sort(arr, start, mid) # 1,14
    m2 = merge_sort(arr, mid+1, end)  #2,19
    output= merge(m1,m2)
    return output

'''
1,2,14,15,18,19,61
'''


print(merge_sort([1,14,2,19,15,18,61], 0, 6))