def sort_flag(arr):
    rp, gp, p = 0, len(arr) - 1, len(arr) - 1
    while p >= rp:
        while arr[rp] == "R":
            rp += 1
        while arr[gp] == "G":
            gp -= 1

        if arr[p] == "R":
            arr[rp], arr[p] = arr[p], arr[rp]
            rp += 1
        if arr[p] == "G":
            arr[gp], arr[p] = arr[p], arr[gp]
            gp -= 1
        if arr[p] == "B":
            p -= 1
    return arr


print(sort_flag(["R", "G", "G", "B", "R", "G", "B"]))
