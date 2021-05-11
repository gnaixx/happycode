#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

from typing import List

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        pointer = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if pointer[i][j]==1:
                    continue
                matrix[i][j], matrix[j][n-1-i] = matrix[j][n-1-i], matrix[i][j]
                pointer[i][j], pointer[j][n-1-i] = 1, 1
# @lc code=end

Solution().rotate([[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]])