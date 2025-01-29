# https://www.geeksforgeeks.org/find-common-elements-three-sorted-arrays/

# time complexity O(n) - where n is the largest array of 3 arrays
# space complexity O(1) - not considering the output array
def find_intersection(arr1, arr2, arr3):
    p2, p3 = 0, 0
    output = []
    for p1, num in enumerate(arr1):
        if p2 >= len(arr2) or p3 >= len(arr3):
            break
        while arr2[p2] < num and p2 < len(arr2) - 1:
            p2 += 1
        while arr3[p3] < num and p3 < len(arr3) - 1:
            p3 += 1
        if arr1[p1] == arr2[p2] == arr3[p3]:
            output.append(num)
            p2 += 1
            p3 += 1

    return [-1] if len(output) == 0 else output