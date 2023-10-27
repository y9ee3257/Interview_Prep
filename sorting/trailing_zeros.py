"""
Count the number of trailing 0s in factorial of a given number.

Input Format
The first line of input contains T - number of test cases. Its followed by T lines, each containing an integer N.

Output Format
For each test case, print the number of trailing 0s in N!, separated by new line.

Constraints
1 <= T <= 10000
1 <= N <= 1015

Example
Input
3
2
5
100

Output
0
1
24

Explanation
2! = 2 [No trailing zeros]
5! = 120 [Trailing zeros=1]
20! = 2432902008176640000 [Trailing zeros=4]
"""


"""
Approach
To compute the number of trailing zeroes in n!, we need to count the number of factors of 10 in n!. 
Notice that 10 can only be formed by multiplying 2 and 5, and we can always find more factors of 2 than factors of 5 in n!. 
Therefore, it suffices to count the number of factors of 5 in n! to determine the number of trailing zeroes.

Let count = 0 be the variable that keeps track of the number of factors of 5. 
We can count the factors of 5 in n! by computing n/5 + n/25 + n/125 + ... until the quotient becomes 0. 
Each term in the sum corresponds to the number of multiples of 5, 25, 125, ..., that are less than or equal to n.

The final value of count will be the number of trailing zeroes in n!.
"""
import sys

test_cases = sys.stdin.readline()

for test in range(int(test_cases)):
    n = int(sys.stdin.readline())
    count = 0
    while n > 0:
        count += n // 5
        n //= 5
    print(count)
