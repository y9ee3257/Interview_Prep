"""
https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/print-hollow-diamond-pattern?page=0&pageSize=10
Print Hollow Diamond Pattern
Print a hollow diamond pattern using '*'. See examples for more details.

Input Format
The first line of input contains T - the number of test cases. It is followed by T lines, each line contains a single odd integer N - the size of the diamond.

Output Format
For each test case, print the test case number as shown, followed by the diamond pattern, separated by a new line.

Constraints
1 <= T <= 100
3 <= N <= 201

Example
Input
4
3
7
5
15

Sample Output 0
Case #1:
 *
* *
 *
Case #2:
   *
  * *
 *   *
*     *
 *   *
  * *
   *
Case #3:
  *
 * *
*   *
 * *
  *
Case #4:
       *
      * *
     *   *
    *     *
   *       *
  *         *
 *           *
*             *
 *           *
  *         *
   *       *
    *     *
     *   *
      * *
       *
"""
import sys

test_cases = sys.stdin.readline()

for idx in range(0, int(test_cases)):
    num_lines = int(sys.stdin.readline())
    print(f'Case #{idx + 1}:')
    for line_num in range(0, num_lines):
        output = [" "] * num_lines
        mid_index = num_lines // 2
        star_1_pos = abs(mid_index - line_num)
        output[star_1_pos] = "*"
        output[-star_1_pos - 1] = "*"
        print("".join(output))
