def solve_sudoku(board):
    # Replace this placeholder return statement with your code

    def validator(board, cell, val):
        value = str(val)
        cell_row = cell[0]
        cell_column = cell[1]
        # check row
        if value in board[cell_row]:
            return False

        # check column
        for i in range(0, 9):
            if board[i][cell_column] == value:
                return False

        # check block
        start = cell_row - (cell_row % 3)
        end = cell_column - (cell_column % 3)
        for i in range(0, 3):
            for j in range(0, 3):
                if board[start + i][end + j] == value:
                    return False
        return True

    def get_next_empty_cell(board):
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    return i, j
        return ()

    def helper(board):
        next_cell = get_next_empty_cell(board)

        if len(next_cell) == 0:
            return True

        for i in range(1, 10):
            if validator(board, next_cell, i):
                board[next_cell[0]][next_cell[1]] = str(i)
                is_solved = helper(board)
                if is_solved:
                    return True
                board[next_cell[0]][next_cell[1]] = "."

        return False

    helper(board)
    return board


def is_valid_unit(unit):
    # Check if the unit contains only digits from 1 to 9 without repetition
    unit = [i for i in unit if i != '.']  # Ignore empty cells represented by '.'
    return len(unit) == len(set(unit)) and all(1 <= int(i) <= 9 for i in unit)


def is_valid_sudoku(board):
    # Check each row
    for row in board:
        if not is_valid_unit(row):
            return False

    # Check each column
    for col in range(9):
        if not is_valid_unit([board[row][col] for row in range(9)]):
            return False

    # Check each 3x3 subgrid
    for box_row in range(3):
        for box_col in range(3):
            if not is_valid_unit([board[r][c] for r in range(box_row * 3, box_row * 3 + 3)
                                  for c in range(box_col * 3, box_col * 3 + 3)]):
                return False

    return True


def test():
    test_case1 = [[".", ".", ".", ".", ".", ".", ".", "7", "."], ["2", "7", "5", ".", ".", ".", "3", "1", "4"],
                  [".", ".", ".", ".", "2", "7", ".", "5", "."], ["9", "8", ".", ".", ".", ".", ".", "3", "1"],
                  [".", "3", "1", "8", ".", "4", ".", ".", "."], [".", ".", ".", "1", ".", ".", "8", ".", "5"],
                  ["7", ".", "6", "2", ".", ".", "1", "8", "."], [".", "9", ".", "7", ".", ".", ".", ".", "."],
                  ["4", "1", ".", ".", ".", "5", ".", ".", "7"]]
    test_case2 = [[".", ".", "6", ".", ".", "4", ".", ".", "."], [".", "3", ".", ".", "1", ".", ".", "9", "5"],
                  [".", ".", ".", ".", ".", ".", "8", ".", "."], [".", ".", ".", ".", "8", ".", "3", ".", "."],
                  ["4", ".", ".", ".", ".", "1", ".", "8", "2"], [".", "2", ".", ".", ".", ".", "7", ".", "."],
                  [".", ".", ".", ".", ".", ".", ".", ".", "7"], [".", "5", ".", ".", "9", ".", ".", "2", "1"],
                  ["3", ".", ".", "5", ".", ".", ".", ".", "."]]
    test_case3 = [["6", ".", ".", ".", ".", ".", "1", ".", "."], [".", ".", ".", "3", ".", ".", ".", ".", "."],
                  [".", "9", ".", ".", "4", "7", ".", "8", "."], ["9", ".", ".", ".", "5", "3", ".", ".", "6"],
                  [".", ".", ".", "2", ".", ".", ".", "5", "."], [".", "3", ".", "8", ".", ".", ".", ".", "."],
                  [".", "7", ".", ".", "9", "5", ".", "4", "."], [".", ".", "4", ".", ".", ".", ".", ".", "8"],
                  [".", ".", ".", ".", "2", ".", ".", ".", "."]]
    test_case4 = [[".", ".", ".", ".", ".", ".", "7", ".", "."], [".", "4", ".", ".", "3", ".", ".", "6", "5"],
                  [".", ".", "1", ".", ".", "8", ".", ".", "."], [".", "6", ".", ".", "5", ".", ".", "3", "9"],
                  ["4", ".", ".", "6", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "2", "."],
                  ["8", ".", ".", ".", ".", "3", ".", "9", "7"], [".", ".", ".", ".", "7", ".", "4", ".", "."],
                  [".", "9", ".", ".", ".", ".", "2", ".", "."]]
    test_case5 = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                  [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                  ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                  [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                  [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    test_cases = [test_case1, test_case2, test_case3, test_case4, test_case5]

    for test_case in test_cases:
        board = solve_sudoku(test_case)
        for i in range(0, 9):
            print(board[i])
        print(f" is valid = {is_valid_sudoku(board)}")
        print("-----------------------------------")


test()
