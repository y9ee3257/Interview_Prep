# Given a string that may consist of opening and closing parentheses, your task is to check whether or not the string contains valid parenthesization.
#
# The conditions to validate are as follows:
#
# Every opening parenthesis should be closed by the same kind of parenthesis. Therefore, {)and [(]) strings are invalid.
#
# Every opening parenthesis must be closed in the correct order. Therefore, )( and ()(() are invalid.
# Input
# "((((("
# Output
# false
#
# Input
# "(){[{()}]}"
# Output
# true
#
# Input
# "{}[]{}[{}])"
# Output
# false

def is_valid(s):
    stack = []
    for char in s:
        top = stack[-1] if stack else ""
        if ((char == '}' and top == '{') or
                (char == ')' and top == '(') or
                (char == ']' and top == '[')) :
            stack.pop()
        else:
            stack.append(char)

    return True if not stack else False
