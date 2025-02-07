def bubble_sort(arr):
    """
     starting with index 0, swap elements to the right if the number is smaller than current index
     do multiple iterations on the array until all the array is sorted
     For every iteration you will get the largest number to the right most place,
     so you dont have to iterate the whole array next time, every iteration starts with 0 and travers until len(array)-i

     1st iteration
     5 4 3 2 1
     4 5 3 2 1
     4 3 5 2 1
     4 3 2 5 1
     4 3 2 1 5
     2nd iteration
     3 4 2 1 5
     3 2 4 1 5
     3 2 1 4 5
     3rd iteration
     2 3 1 4 5
     2 1 3 4 5
     4th iteration
     1 2 3 4 5
    """
    for idx in range(len(arr)):
        for idx2 in range(len(arr) - idx - 1):
            current = arr[idx2]
            next = arr[idx2 + 1]
            if current > next:
                arr[idx2] = next
                arr[idx2 + 1] = current
    return arr


def insertion_sort(arr):
    """
    take each element and compare with left elements
    if left is greater swap them.
    keep doing this until you find the perfect place for the element
    ex:
    lets take last element as an example
    2 3 4 5 1
    2 3 4 1 5
    2 3 1 4 5
    2 1 3 4 5
    1 2 3 4 5
    """

    for idx, num in enumerate(arr):
        left = idx - 1
        while left >= 0:
            if num <= arr[left]:
                arr[left + 1] = arr[left]
                arr[left] = num
                left -= 1
            else:
                break
    return arr


def merge_sort(arr, start, end):
    """
     you split array into half (left, right) until you have only 1 element left.
     now merge the split arrays at each level by sorting them
        5 4 4 3 2 1
      5 4 4     3 2 1
     5   4 4   3   2 1
        4   4     2   1

       1 2 3 4 4 5    -- final sorted array
     4 4 5    1 2 3   -- merge sorted array  1,2,3 with 4,5
    5  4 4   3   1 2  -- merge sorted array  1,2 with 3


          0 6
    0,3        3,6
  0,1  1,3
 0,0 0,1

    """
    if len(arr) == 0:
        return arr
    if start == end:
        return [arr[start]]

    mid = start + (end - start) // 2
    left_sorted = merge_sort(arr, start, mid)
    right_sorted = merge_sort(arr, mid + 1, end)
    return merge_sorted_arrays(left_sorted, right_sorted)


def selection_sort(arr):
    """
    just like inserting sort, but while iterating through the array
        swap the current index with lowest number in the remaining array
    ex:
    5,4,3,2,1 -- swap 1,5
    1,4,3,2,5 -- swap 4,2
    1,2,3,4,5 -- no swap needed at 3, as there is no small element to the right
    """
    for idx, num in enumerate(arr):
        pointer = idx + 1
        small_index = idx
        while pointer < len(arr):
            if arr[pointer] < arr[small_index]:
                small_index = pointer
            pointer += 1
        arr[idx] = arr[small_index]
        arr[small_index] = num

    return arr


def quick_sort(arr, start, end):
    """
     quick sort is very similar to merge sort, just that this chooses a pivot instead of bisecting the array

     quick sort chooses a pivot, all elements less than pivot will be placed to the left of pivot
     and all elements greater than pivot will be placed right of pivot.
     call quick sort recursively for the left array and right array, merge both sorted arrays.
     ex:
     5 2 1 3 4 7 6
     pivot = 3
            1) 2 1 3 <- 4 -> 5 7 6   --- choosing 4 as pivot
            2) 1 <-2-> 3     5 <-6-> 7
            3) 1 2 3 4 5 6 7
    """

    if start <= end:
        return
    # choose pivot as mid element
    pivot = start + (end - start) // 2
    pivot_num = arr[pivot]

    arr[pivot], arr[end] = arr[end], arr[pivot]
    left, right = start, end - 1

    print(f"pivot = {pivot}")
    print(f"arr = {arr}")

    while left < right:
        if arr[left] <= pivot_num:
            left += 1
        elif arr[right] >= pivot_num:
            right -= 1
        else:
            print(f"swapping left and right,  left = {left}, right ={right}")
            arr[left], arr[right] = arr[right], arr[left]

    arr[left], arr[end] = arr[end], arr[left]
    print(f"calling quick_sort for indexes start={start}, end={left - 1}")
    quick_sort(arr, start, left - 1)
    print(f"calling quick_sort for indexes start={left + 1}, end={end}")
    quick_sort(arr, left + 1, end)


def merge_sorted_arrays(arr1, arr2):
    """
     [1 2 3 4 5]
                   = [1 2 3 3 4 4 5 5 6 7]
     [3 4 5 6 7]
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


def find_intersection(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
     {
        "arr1": [2, 5, 10],
        "arr2": [2, 3, 4, 10],
        "arr3": [2, 4, 10]
     }
    """
    # compare arr1 and arr2 with 2 pointers
    # compare the output with arr3

    p1 = 0
    p2 = 0
    common_elements = []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            p1 += 1
        elif arr1[p1] > arr2[p2]:
            p2 += 1
    else:
        common_elements.append(arr1[p1])
        p1 += 1

    p1 = 0
    p2 = 0
    final_common = []

    while p1 < len(common_elements) and p2 < len(arr3):
        if common_elements[p1] < arr3[p2]:
            p1 += 1
        elif common_elements[p1] > arr3[p2]:
            p2 += 1
        else:
            final_common.append(common_elements[p1])
            p1 += 1

    return final_common


def quick_sort2(arr):
    array_copy = arr
    quick_sort_helper(array_copy, 0, len(arr) - 1)
    return array_copy


def quick_sort_helper(arr, start, end):
    if len(arr) == 0 or start < 0 or end > len(arr) - 1 or start >= end:
        return

    pivot_index = start + (end - start) // 2
    pivot = arr[pivot_index]
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    left, right = start, end - 1
    while left < right:
        if arr[left] <= pivot:
            left += 1
        elif arr[right] >= pivot:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]

    if arr[right] > arr[end]:
        arr[end], arr[right] = arr[right], arr[end]
    else:
        right = end

    quick_sort_helper(arr, start, right - 1)
    quick_sort_helper(arr, right + 1, end)


def run(input_array):
    print(f"bubble sort    {bubble_sort([*input_array])}")
    print(f"insertion sort {insertion_sort([*input_array])}")
    print(f"merge sort     {merge_sort([*input_array], 0, len(input_array) - 1)}")
    print(f"selection sort {selection_sort([*input_array])}")
    print(f"quick sort     {quick_sort2([*input_array])}")
    print("----------------------------------")


inputs = [[6, 3, 4, 1, 4, 2], [1, 2, 3, 4, 5, 6], [7, 6, 5, 4, 3, 2], [3], [3, 4, 6, 6, 7, 4, 4, 6, 6, 6, 3],
          [3, 3, 3, 3, 3, 3, 3, 3], []]

for arr in inputs:
    run(arr)

# print(quick_sort2([7, 6, 5, 4, 3, 2]))
