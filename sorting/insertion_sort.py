arr = [5, 2, -56, 2, 34, 3]

print("input", arr)

for i in range(1, len(arr)):
    current = arr[i]
    empty_index = None
    for j in range(i - 1, -1, -1):
        if arr[j] > current:
            arr[j + 1] = arr[j]
            empty_index = j
        else:
            break
    if empty_index is not None:
        arr[empty_index] = current

print("output", arr)
