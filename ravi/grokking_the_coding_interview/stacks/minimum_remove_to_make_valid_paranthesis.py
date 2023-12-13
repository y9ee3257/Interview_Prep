# https://www.educative.io/courses/grokking-coding-interview-patterns-python/minimum-remove-to-make-valid-parentheses
# Given a string, s, that may have matched and unmatched parentheses,
# remove the minimum number of parentheses so that the resulting string represents a valid parenthesization.
# For example, the string “a(b)” represents a valid parenthesization while the string “a(b” doesn’t,
# since the opening parenthesis doesn’t have any corresponding closing parenthesis.
#
# Input
# "ab)ca(so)(sc(s)("
# Output
# "abca(so)sc(s)"
# Input
# ")("
# Output
# ""
# Input
# "()"
# Output
# "()"
# Input
# "("
# Output
# ""

from collections import deque
def min_remove_parentheses(s):

    # count number of open and close parantesis putting in the stack.
    # while inseting if the closing is greater than open do not insert that closing one
    # Similarly go in opposite direction to remove invalid open parantesis
    stack = deque()
    open_count,close_count = 0,0
    for char in s:
        if char == '(':
            open_count+=1
        elif char == ')':
            if close_count<open_count:
                close_count+=1
            else:
                continue
        stack.append(char)
    open_count,close_count = 0,0
    print(stack)
    output = []
    while len(stack)>0:
        top = stack.pop()
        if top == ')':
            close_count+=1
            output.append(top)
        elif top == '(':
            if open_count<close_count:
                open_count+=1
                output.append(top)
        else:
            output.append(top)
    output.reverse()
    return "".join(output)


# push only the parentheses with indexes to the stack. keep poping when you find a valid set.
# In the end only the invalid parantesis remain in the stack
def min_remove_parentheses_effective(s):
    stack = deque()
    for idx,char in enumerate(s):
        obj = {"char":char,"idx":idx}
        if char=="(":
            stack.append(obj)
        elif char == ")":
            if len(stack)!=0 and stack[-1]["char"]=="(":
                stack.pop()
            else:
                stack.append(obj)
    output = list(s)
    while len(stack)>0:
        top = stack.pop()
        output[top["idx"]]=""
    return "".join(output)







inputs = ['a(sss9(ss(ss)',"99((()","()()()"]
for input in inputs:
    print(min_remove_parentheses(input))


























