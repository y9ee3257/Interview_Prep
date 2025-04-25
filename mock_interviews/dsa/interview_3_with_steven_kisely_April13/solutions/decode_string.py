"""
https://leetcode.com/problems/decode-string/description/
"""


def decode(input):
    input = list(input)
    stack = []
    while input:
        if not input[-1].isdigit():
            stack.append(input.pop())
        else:
            digits = ""
            while input and input[-1].isdigit():
                digits += input.pop()
            count = int(digits[::-1])
            curr_string = ""
            while stack and stack[-1] != "]":
                top_char = stack.pop()
                if top_char != "[":  # cd
                    curr_string += top_char
            stack.pop()
            new_str = ""
            for _ in range(count):
                new_str += curr_string
            stack.append(new_str)
    output = ""
    for _ in range(len(stack)-1,-1,-1):
        output += stack.pop()
    return output


s = "3[a]2[bc]"
print(decode(s))
s = "3[a2[c]]"
print(decode(s))
s = "2[abc]3[cd]ef"
print(decode(s))
