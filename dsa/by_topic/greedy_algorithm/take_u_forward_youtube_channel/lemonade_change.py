"""
https://leetcode.com/problems/lemonade-change/
"""


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        fives, tens = 0, 0

        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives == 0:
                    return False
                fives -= 1
                tens += 1
            elif bill == 20:
                change = 15
                while change > 0:
                    if (tens == 0 and fives == 0) or (change == 5 and fives == 0):
                        return False
                    if tens > 0:
                        tens -= 1
                        change -= 10
                    if fives > 0:
                        fives -= 1
                        change -= 5

        return True




