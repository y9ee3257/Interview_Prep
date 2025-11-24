# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        # edge cases
        # 1. spaces between numbers ex: "  -88827   5655  U"
        # 2. for i range(len(s)) will have issues at s[:i] since i will not go beyond len(s)
        # 3. float values: "3.14159" --> int(num) will not work
        # 4. values with + sign ex: "+345"

        s = s.strip()
        is_negative = 1
        if len(s) > 0 and (s[0] == "-" or s[0] == "+"):
            is_negative = -1 if s[0] == "-" else 1
            s = s[1:]

        i = 0
        while i < len(s):
            if not s[i].isdigit():
                break
            i += 1
        try:
            s_num = s[:i]
            print(s_num)
            s_num = is_negative * int(float(s_num))

            if s_num < -pow(2, 31):
                return -pow(2, 31)
            elif s_num > pow(2, 31) - 1:
                return pow(2, 31) - 1
            return s_num
        except:
            return 0

