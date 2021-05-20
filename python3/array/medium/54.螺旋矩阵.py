#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

from typing import List

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return list(matrix.pop(0)) + self.spiralOrder(list(zip(*matrix))[::-1]) if matrix else []
# @lc code=end

Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])