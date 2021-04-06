#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

from typing import List

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        for i in range(0, numRows):
            row = []
            for j in range(0, i+1):
                if j==0 or j==i:
                    row.append(1)
                else:
                    row.append(rows[i-1][j-1] + rows[i-1][j])
            rows.append(row)
        return rows
# @lc code=end

print(Solution().generate(5))