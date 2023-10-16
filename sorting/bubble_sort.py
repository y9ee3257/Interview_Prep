arr = [9, 5, 3, 4, 12, 34, 11]

print("input", arr)
for i in range(len(arr), 0, -1):
    for j in range(i-1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("output", arr)
