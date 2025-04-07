"""
Generate All Possible Expressions That Evaluate To The Given Target Value
Given a string s that consists of digits ("0".."9") and target, a non-negative integer, find all expressions that can be built from string s that evaluate to the target.

When building expressions, you have to insert one of the following operators between each pair of consecutive characters in s: join or * or +. For example, by inserting different operators between the two characters of string "12" we can get either 12 (1 joined with 2 or "12") or 2 ("1*2") or 3 ("1+2").

Other operators such as - or ÷ are NOT supported.

Expressions that evaluate to the target but only utilize a part of s do not count: entire s has to be consumed.

Precedence of the operators is conventional: join has the highest precedence, * – medium and + has the lowest precedence. For example, 1 + 2 * 34 = (1 + (2 * (34))) = 1 + 68 = 69.

You have to return ALL expressions that can be built from string s and evaluate to the target.

Example
{
"s": "202",
"target": 4
}
Output:

["2+0+2", "2+02", "2*02"]
Same three strings in any other order are also a correct output.

Notes
Order of strings in the output does not matter.
If there are no expressions that evaluate to target, return an empty list.
Returned strings must not contain spaces or any characters other than "0",..., "9", "*", "+".
All returned strings must start and end with a digit.
Constraints:

1 <= length of s <= 13
1 <= target <= 1013
"""


def generate_all_expressions(s, target):
    """
    Args:
     s(str)
     target(int64)
    Returns:
     list_str
    """
    output = []

    def sanitize(expression):
        num = ""
        output = ""
        for char in expression:
            if char.isdigit():
                num += char
            else:
                if num:
                    output += str(int(num))
                output += char
                num = ""
        if num:
            output += str(int(num))
        return output

    def helper(slate, index):
        if index >= len(s):
            exp = "".join(slate)
            sanitized_exp = sanitize(exp)
            evaluated = eval(sanitized_exp)
            if evaluated == target:
                output.append(exp)
            return

        char = s[index]

        # when its the last char, no operations can be done for the next char.
        # so just append it. This also avoids having "+,*" towards the end of slate.
        if index == len(s) - 1:
            slate.append(char)
            helper(slate, index + 1)
            slate.pop()
        else:
            slate.append(char + "+")
            helper(slate, index + 1)
            slate.pop()

            slate.append(char + "*")
            helper(slate, index + 1)
            slate.pop()

            slate.append(char)
            helper(slate, index + 1)
            slate.pop()

    helper([], 0)
    return output