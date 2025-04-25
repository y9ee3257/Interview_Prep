"""
https://neetcode.io/problems/palindrome-partitioning
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        output = []

        def isPalindrome(s):
            return s == s[::-1]
        # []
        def helper(slate, index): # ["aab","a"], 3
            # check if last element in slate is palendrome
            # [[a][ba]]
            if index == len(s):
                if slate and isPalindrome(slate[-1]):
                    print(slate)
                    output.append(slate[:])
                    # print(output)
                return

            curr = s[index] # b

            # append as a new array to slate
            # check if last element is palindrome
            # ["a","ab"]
            if not slate or isPalindrome(slate[-1]):
                slate.append(curr)
                helper(slate, index+1) # [], 0
                slate.pop()

            # append to the last array
            # ["a","ab"]c
            if slate:
                slate[-1] = slate[-1]+ curr
                helper(slate, index+1) #["a","ab"], 3
                # slate[-1] = slate[:len]

        helper([],0)
        return output

# s = "abc"
# s.append(d)



