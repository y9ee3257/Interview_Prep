# https://www.hackerrank.com/challenges/richie-rich/problem?isFullScreen=true
#
# Palindromes are strings that read the same from the left or right, for example madam or 0110.
#
# You will be given a string representation of a number and a maximum number of changes you can make. Alter the string,
# one digit at a time, to create the string representation of the largest number possible given the limit to the number of changes.
# The length of the string may not be altered, so you must consider 's left of all higher digits in your tests. For example  is valid,  is not.
#
# Given a string representing the starting number, and a maximum number of changes allowed,
# create the largest palindromic string of digits possible or the string '-1' if it is not possible to create a palindrome under the contstraints.
#
# Example
#
#
# Make  replacements to get .
#
#
#
# Make  replacement to get .
#
# Function Description
#
# Complete the highestValuePalindrome function in the editor below.
#
# highestValuePalindrome has the following parameter(s):
#
# string s: a string representation of an integer
# int n: the length of the integer string
# int k: the maximum number of changes allowed
# Returns
#
# string: a string representation of the highest value achievable or -1
# Input Format
#
# The first line contains two space-separated integers,  and , the number of digits in the number and the maximum number of changes allowed.
# The second line contains an -digit string of numbers.
#
# Constraints
#
# Each character  in the number is an integer where .
# Output Format
#
# Sample Input 0
#
# STDIN   Function
# -----   --------
# 4 1     n = 4, k = 1
# 3943    s = '3943'
# Sample Output 0
#
# 3993
# Sample Input 1
#
# 6 3
# 092282
# Sample Output 1
#
# 992299
# Sample Input 2
#
# 4 1
# 0011
# Sample Output 2
#
# -1
# Explanation
#
# Sample 0
#
# There are two ways to make  a palindrome by changing no more than  digits:
#


def highestValuePalindrome(s, n, k):
    left, right, min_changes = 0, n - 1, 0
    while left < right:
        if s[left] != s[right]:
            min_changes += 1
        left += 1
        right -= 1

    remaining = k - min_changes
    if remaining < 0:
        return "-1"

    left, right = 0, n - 1
    while left < right:
        has_max = s[left] == '9' or s[right] == '9'

        if s[left] != s[right]:
            value = str(max(int(s[left]), int(s[right])))
            if remaining > 0 or (has_max and remaining == 0):
                value = "9"
                remaining -= 0 if has_max else 1
            s = s[:left] + value + s[left + 1:]
            s = s[:right] + value + s[right + 1:]
            min_changes -= 1

        elif not has_max and remaining > 1:
            s = s[:left] + "9" + s[left + 1:]
            s = s[:right] + "9" + s[right + 1:]
            remaining -= 2

        left += 1
        right -= 1

    if remaining > 0:
        s = s[:left] + "9" + s[left + 1:]
    return s
