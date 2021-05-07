#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

from typing import List

# @lc code=start
class Solution:
    # 判断数组是否有重复
    def isUnitValid(self, unit: List[str]) -> bool:
        unit = [s for s in unit if s!='.']
        return len(set(unit)) == len(unit)

    # 判断行是否有重复
    def isRowValid(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isUnitValid(row):
                return False
        return True

    # 判断列是否有重复
    def isColValid(self, board: List[List[str]]) -> bool:
        for col in list(zip(*board)):
            if not self.isUnitValid(col):
                return False
        return True

    # 判断矩阵是否重复
    def isSquareValid(self, board: List[List[str]]) -> bool:
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                unit = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.isUnitValid(unit):
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isRowValid(board) and self.isColValid(board) and self.isSquareValid(board)
# @lc code=end

Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])