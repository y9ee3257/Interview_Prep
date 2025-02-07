# https://interviewkickstart.com/blogs/problems/letter-combinations-of-a-phone-number


output = []
def helper(phone_number, idx, slate):
    if idx == len(phone_number):
        output.append("".join(slate))
        return

    if phone_number[idx] == "1" or phone_number[idx] == "0":
        helper(phone_number, idx + 1, slate)
        return

    for char in get_chars(phone_number[idx]):
        slate.append(char)
        helper(phone_number, idx + 1, slate)
        slate.pop()


def get_chars(letter):
    dict = {"2": ["a", "b", "c"],
            "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
    return dict[letter]


def get_words_from_phone_number(phone_number):
    """
    Args:
     phone_number(str)
    Returns:
     list_str
    """
    helper(phone_number, 0, [])
    return output