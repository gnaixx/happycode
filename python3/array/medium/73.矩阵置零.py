#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

from typing import List
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # r, c, row, col = len(matrix), len(matrix[0]), [], []
        # for i in range(r):
        #     for j in range(c):
        #         if matrix[i][j]==0:
        #             row.append(i), col.append(j)
        # for i in range(r):
        #     for j in range(c):
        #         if i in row or j in col:
        #             matrix[i][j] = 0
        m, n = len(matrix), len(matrix[0])
        flag_col0 = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                flag_col0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        # 防止第一行被提前修改，倒序遍历
        for i in range(m - 1, -1, -1):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag_col0:
                matrix[i][0] = 0
# @lc code=end

Solution().setZeroes([[1,0,1],[1,0,1],[1,1,1]])