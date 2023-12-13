# https://www.educative.io/courses/grokking-coding-interview-patterns-python/repeated-dna-sequences
#
# Given a string, s, that represents a DNA subsequence, and a number k
# ,return all the contiguous subsequences (substrings) of length k
# that occur more than once in the string. The order of the returned subsequences does not matter.
# If no repeated substring is found, the function should return an empty set.
#
# Input
# "AAAAACCCCCAAAAACCCCCC" , 8
# Output
# ["AAAACCCC", "AAAAACCC", "AAACCCCC"]
# Input
# "GGGGGGGGGGGGGGGGGGGGGGGGG" , 9
# Output
# ["GGGGGGGGG"]
# Input
# "ATATATATATATATAT" , 6
# Output
# ["ATATAT", "TATATA"]
# Input
# "AAAAAACCCCCCCAAAAAAAACCCCCCCTG" , 10
# Output
# ["AAAAAACCCC", "AAAAACCCCC", "AAAACCCCCC", "AAACCCCCCC"]

def find_repeated_sequences(s, k):
    left, right = 0, 0
    hash_values = set()
    output_set = set()
    while right < len(s):
        cur_length = right - left + 1
        if cur_length < k:
            right += 1
        elif cur_length == k:
            current_substring = s[left:right + 1]
            hash_value = hash(current_substring)
            if hash_value in hash_values:
                output_set.add(current_substring)
            else:
                hash_values.add(hash_value)

            left += 1
            right += 1

    return output_set


print(find_repeated_sequences("aabcdeaabcde",3))