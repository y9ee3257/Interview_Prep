# https://www.educative.io/courses/grokking-coding-interview-patterns-python/first-bad-version
#
# The latest version of a software product fails the quality check. Since each version is developed upon the previous
# one, all the versions created after a bad version are also considered bad.
#
# Suppose you have n versions with the IDs [1,2,...,n]
# , and you have access to an API function that returns TRUE if the argument is the ID of a bad version.
#
# Find the first bad version that is causing all the later ones to be bad. Additionally, the solution should also
# return the number of API calls made during the process and should minimize the number of API calls too.
# Input 100
# Output [67, 7]
#
# Input 13
# Output [10, 3]

from api import *

version_api = api(0)


def is_bad_version(v):
    return version_api.is_bad(v)


def first_bad_version(n):
    # -- DO NOT CHANGE THIS SECTION
    version_api.n = n
    # --

    left = 1
    right = n
    first_bad_version = n
    api_calls = 0
    while left < right:
        mid = (left + right) // 2
        if is_bad_version(mid):
            first_bad_version = min(first_bad_version, mid)
            right = mid
        else:
            left = mid + 1
        api_calls += 1
    return first_bad_version, api_calls
