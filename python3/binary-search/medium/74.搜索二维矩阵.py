#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

from typing import List

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        s, e = 0, r*c-1
        while s <= e:
            m = (s + e) >> 1
            num = matrix[int(m/c)][int(m%c)]
            if num == target:
                return True
            if target > num:
                s = m + 1
            else:
                e = m - 1
        return False
# @lc code=end

Solution().searchMatrix([[1,1]], 13)