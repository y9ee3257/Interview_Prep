# Tip: You may use some of the code templates provided
# in the support files

def solve_n_queens(n):
    forward_diag = set()
    backward_diag = set()
    columns = set()
    board = [["." for _ in range(n)] for _ in range(n)]
    output = []

    def helper(row):
        if row >= n:
            output.append([b.copy() for b in board])
            return
        for col in range(0, n):
            if row + col not in forward_diag and row - col not in backward_diag and col not in columns:
                board[row][col] = 'Q'
                forward_diag.add(row + col)
                backward_diag.add(row - col)
                columns.add(col)

                helper(row + 1)

                board[row][col] = '.'
                forward_diag.remove(row + col)
                backward_diag.remove(row - col)
                columns.remove(col)

    helper(0)

    return output


for i in range(10):
    print(f"i: {i}, res: {solve_n_queens(i)}")
