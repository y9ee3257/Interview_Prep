# https://leetcode.com/problems/sudoku-solver/
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        backtracking(self,0,0,board)


    def backtracking(self, row_index, col_index, board:List[List[str]]):
        next_cell = get_next_cell(self,row_index,col_index)
        if board[row_index][col_index] == ".":
            for number in range(1,9):
                board[row_index][col_index]=number
                if is_valid(self,row_index,col_index,number,board):
                    if next_cell == None:
                        return
                    backtracking(self,next_cell.row_index,next_cell.col_index,board)
                else:
                    board[row_index][col_index]="."
        else:
            if next_cell == None:
                return
            backtracking(self,next_cell.row_index,next_cell.col_index,board)


    def get_next_cell(self, row_index, col_index):
        if row_index ==9 and col_index ==9 :
            return None
        if col_index<9:
            return {row_index,col_index:col_index+1}
            elif row_index<9:
            return {row_index:row_index+1,col_index}



    def is_valid(self,row_index, col_index, value, board: List[List[str]]):
        for current_row, row in enumerate(board):
            for current_col, cell in enumerate(row):
                if row_index == current_row and col_index == current_col:
                    continue
                elif row_index == current_row or current_col == col_index:
                    if cell == str(value):
                        return False
                else:
                    row_block_start = (row_index / 3) * 3
                    row_block_end = row_block_start + 2
                    col_block_start = (col_index / 3) * 3
                    col_block_end = col_block_start + 2
                    if row_block_start <= current_row <= row_block_end and col_block_start <= current_col <= col_block_end and cell == str(value):
                        return False
        return True


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(is_valid(0,0,6,board))