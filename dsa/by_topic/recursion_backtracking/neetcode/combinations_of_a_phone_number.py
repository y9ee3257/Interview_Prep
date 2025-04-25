"""
https://neetcode.io/problems/combinations-of-a-phone-number
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        output = []
        char_map = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        if not digits:
            return []

        def helper(slate, index):
            if index == len(digits):
                output.append("".join(slate))
                return

            curr = int(digits[index]) # 3

            for char in char_map[curr]: # DEF
                slate.append(char)
                helper(slate, index+1)
                slate.pop()

        helper([],0)
        return output







