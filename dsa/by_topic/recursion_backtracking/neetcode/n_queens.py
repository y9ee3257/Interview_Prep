"""
https://neetcode.io/problems/n-queens
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        output = []
        slate = [["." for _ in range(n)] for _ in range(n)]
        # print(slate)

        def helper(slate,row_index, col_set, diag1_set, diag2_set):
            # print(slate)
            # print(row_index)
            # print("...................")
            # [".",".",".","Q"] --> ["...Q"]
            if row_index == n:
                output.append(["".join(x) for x in slate])
                return


            for col_index in range(n):
                diag1_index = row_index - col_index
                diag2_index = row_index + col_index
                # condigions to place a queen in this cell
                # check col_set, diag1_map, diag2_map
                if col_index not in col_set and diag1_index not in diag1_set and diag2_index not in diag2_set:
                    # update col_set, diag1_map, diag2_map
                    col_set.add(col_index)
                    diag1_set.add(diag1_index)
                    diag2_set.add(diag2_index)
                    slate[row_index][col_index]="Q"

                    helper(slate, row_index+1, col_set, diag1_set, diag2_set)

                    col_set.remove(col_index)
                    diag1_set.remove(diag1_index)
                    diag2_set.remove(diag2_index)
                    slate[row_index][col_index]="."

        helper(slate,0,set(),set(),set())
        return output





