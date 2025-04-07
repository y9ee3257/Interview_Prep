"""
N Queen Problem
Given an integer n, find all possible ways to position n queens on an n×n chessboard so that no two queens attack each other. A queen in chess can move horizontally, vertically, or diagonally.

Do solve the problem using recursion first even if you see some non-recursive approaches.

Example One
{
"n": 4
}
Output:

[
["--q-",
 "q---",
 "---q",
 "-q--"],

["-q--",
 "---q",
 "q---",
 "--q-"]
]
There are two distinct ways four queens can be positioned on a 4×4 chessboard without attacking each other. The positions may appear in the output in any order. So the same two positions in different order would be another correct output.

Example Two
{
"n": 2
}
Output:

[
]
No way to position two queens on a 2×2 chessboard without them attacking each other - so empty array.

Notes
The function must return a two-dimensional array of strings representing the arrangements. Size of the array must be m×n where m is the number of distinct arrangements.

Each string must be n characters long, and the strings' characters may be either q (for a queen) or - (for an empty position on the chessboard). Valid arrangements may appear in the output in any order.

Constraints:

1 <= n <= 12
"""


def find_all_arrangements(n):
    """
    Everytime you set a queen, mark that particular row,column, 2 diagonals to true, so you don't have to set queen on every single index and do a test.

    00 01 02
    10 11 12
    20 21 22

    for diagonals resembling backslash (\) the commonality is (row-col) is always same. So named it diag_set_sub (make sure its twice the size of n)
        ex: 00,11,22 = 0
            01,12     = -1
            02         = -2
    for diagonals resembling forwardslash (/) the commanility is (row+col) is always same. so named it diag_set_add (make sure its twice the size of n)
            20,11,02 = 2
            10, 01   = 1
            00       = 0
    """
    output = []
    row_set = [0] * n
    col_set = [0] * n
    diag_set_sub = [0] * 2 * n
    diag_set_add = [0] * 2 * n

    def setQueen(slate, row):
        if row >= n:
            output.append(["".join(row) for row in slate])
            return

        for col in range(n):
            diff = row - col
            sum = row + col
            if row_set[row] == 0 and col_set[col] == 0 and diag_set_sub[diff] == 0 and diag_set_add[sum] == 0:
                row_set[row], col_set[col], diag_set_sub[diff], diag_set_add[sum] = 1, 1, 1, 1
                slate[row][col] = "q"
                setQueen(slate, row + 1)
                slate[row][col] = "-"
                row_set[row], col_set[col], diag_set_sub[diff], diag_set_add[sum] = 0, 0, 0, 0

    slate = [["-"] * n for i in range(n)]
    setQueen(slate, 0)
    return output
