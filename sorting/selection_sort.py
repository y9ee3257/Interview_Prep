# https://1drv.ms/o/s!ArqWk5IiXXCEbxNUVQer2i1Z190?e=3XW01L

arr = [5, 3, 4, -10, 34, 2, 7]

print("input", arr)
for i in range(len(arr)):
    min = arr[i]
    min_index = i
    for j in range(i, len(arr)):
        if arr[j] < min:
            min = arr[j]
            min_index = j
    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp

print("output", arr)
