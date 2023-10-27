"""
https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/print-right-angled-triangle-pattern?page=0&pageSize=10
Print Right Angled Triangle Pattern
Print a mirror image of a right-angled triangle using '*'. See examples for more details.

Input Format
The First line of input contains T - the number of test cases. It's followed by T lines, each line contains a single integer N - the size of the pattern.

Output Format
For each test case, print the test case number as shown, followed by the pattern, separated by a newline.

Constraints
1 <= T <= 100
1 <= N <= 100

Example
Input
4
2
1
5
10

Output
Case #1:
 *
**
Case #2:
*
Case #3:
    *
   **
  ***
 ****
*****
Case #4:
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********

"""
import sys

test_cases = sys.stdin.readline()

for idx in range(0, int(test_cases)):
    num_lines = int(sys.stdin.readline())
    print(f'Case #{idx + 1}:')
    for star_count in range(1, num_lines + 1):
        output = ""
        space_count = num_lines - star_count
        for j in range(0, num_lines):
            if space_count <= 0:
                output += "*"
            else:
                output += " "
                space_count -= 1
        print(output)
