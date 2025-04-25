"""
Given a 2D grid, each cell contains a human 0, zombie 1, or wall 2 (numbers 0, 1, 2).
Zombies can turn adjacent (up/down/left/right) human beings into zombies every day, but cannot go through walls.
How long will it take to turn all people into zombies? Return -1 if not all humans are turned into zombies.
Main example
Input:
[[1, 0, 0, 0, 1],
 [0, 0, 0, 0, 0]]
Output: 3
Explanation:
At the end of the 1st day, the status of the grid:
[[1, 1, 0, 1, 1],
 [1, 0, 0, 0, 1]]
At the end of the 2nd day, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 0, 1, 1]]
At the end of the 3rd day all humans have been converted to zombies.
Wall example
Input:
[[2, 1],
 [0, 2]]
Output: -1
"""


from collections import deque


def zombie_convert(matrix):
    if len(matrix) == 0:
        return -1

    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    human_count = 0
    q = deque()
    rl = len(matrix)
    cl = len(matrix[0])

    for row_i, row in enumerate(matrix):
        for col_i,cell in enumerate(row):
            if cell == 0:
                human_count +=1
            elif cell == 1:
                q.append((row_i,col_i))


    days = 0

    while q:
        zombie_count = len(q)
        days+=1

        for _ in range(zombie_count):
            row,col = q.popleft()

            for dirX , dirY in directions:
                new_row, new_col = row+ dirX, col+dirY
                if 0<=new_row<rl and 0<=new_col<cl and matrix[new_row][new_col] == 0:
                    matrix[new_row][new_col]=1
                    q.append(matrix[new_row][new_col])
                    human_count -=1

    if human_count ==0:
        return days

    return -1






"""

Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the original data does not contain any digits and that digits are only 
for those repeat numbers, k. For example, there won't be input like 3a or 2[4]
Input will always be valid and consists of lowercase english letters, digits, and square brackets [ ]
 
All integers will be in the range [1, 300]
1 <= s.length <= 30
Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:
Input: 2 = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
    
    
3[a2[c]]    
    
[cd]xyz

300

xyz

x
y
z

zyx - "".join(stack) -> "zyx"


2[abc]3[cd]ef




ef cdcdcd abcabcabc


abcabcabc cdcdcd ef
"""



def decode(input):


    stack = []

    #abc3[cd]xyz

    #  cdcdcdzyx
    while input:

        if not input[-1].isdigit():
            stack.push(input.pop())
        else:
            digits = ""

            #300   003 -> int(300)
            while input[-1].isdigit():
                digits += input.pop()

            count = int(digits.reverse())

            curr_string = ""
            while stack[-1] == "]":
                top_char = stack.pop()

                if top_char != "[":  # cd
                    curr_string += top_char


            for _ in range(count):
                curr_string+=curr_string


            stack.push(curr_string)


    output = ""

    for char in range(len(stack)-1,0,-1):
        output+=stack.pop()

    return output








































































































