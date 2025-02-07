output = []


def helper(input_arr, slate):
    if len(input_arr) == 0:
        output.append(slate[:])
        return

    for i,element in enumerate(input_arr):
        slate.append(element)
        helper(input_arr[:i]+input_arr[i+1:], slate)
        slate.pop()


def generate_all_permutations(arr):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    helper(arr, [])
    return output


res = generate_all_permutations([1, 2, 3, 4, 5])

res.sort(key=lambda x: len(x))
print(len(res))
print(res)