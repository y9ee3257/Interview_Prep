# Dutch National Flag
# Given some balls of three colors arranged in a line, rearrange them such that all the red balls go first, then green and then blue ones.
#
# Do rearrange the balls in place. A solution that simply counts colors and overwrites the array is not the one we are looking for.
#
# This is an important problem in search algorithms theory proposed by Dutch computer scientist Edsger Dijkstra. Dutch national flag has three colors (albeit different from ones used in this problem).
#
# Example
# {
#     "balls": ["G", "B", "G", "G", "R", "B", "R", "G"]
# }
# Output:
#
# ["R", "R", "G", "G", "G", "G", "B", "B"]
# There are a total of 2 red, 4 green and 2 blue balls. In this order they appear in the correct output.

# time complexity O(n)
# space complexity O(1)
def dutch_flag_sort(balls):
    p1, p2, index = 0, len(balls) - 1, 0

    while p1 < p2 and index < len(balls):
        if balls[index] == 'R' and index > p1:
            balls[index], balls[p1] = balls[p1], balls[index]
            p1 += 1
        elif balls[index] == 'B' and index < p2:
            balls[index], balls[p2] = balls[p2], balls[index]
            p2 -= 1
        else:
            index += 1

    return balls