#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

from typing import List

# @lc code=start
class Solution:
    # 54 的反向操作
    # [] -> [[9]] -> [[8],[9]] -> [[6,7],[9,8]] -> [[4,5],[9,6],[8,7]] -> [[1,2,3],[8,9,4],[7,6,5]]
    def generateMatrix1(self, n: int) -> List[List[int]]:
        matrix, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo-len(matrix), lo
            matrix = [[i for i in range(lo, hi)]] + list(zip(*matrix[::-1]))
        return matrix
    
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A
    
# @lc code=end

Solution().generateMatrix(3)