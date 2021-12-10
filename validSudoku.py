# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            tmp = ''.join(board[i])
            tmp = tmp.replace('.', '')
            if len(tmp) != len(set(tmp)):
                return False
        for i in range(9):
            tmp = ''.join(board[j][i] for j in range(9))
            tmp = tmp.replace('.', '')
            if len(tmp) != len(set(tmp)):
                return False
        for i in range(3):
            for j in range(3):
                tmp = ''.join(board[3*i+m][3*j+n] for m in range(3) for n in range(3))
                tmp = tmp.replace('.', '')
                if len(tmp) != len(set(tmp)):
                    return False
        return True
