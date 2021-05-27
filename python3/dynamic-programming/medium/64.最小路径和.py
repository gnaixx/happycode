#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

from typing import List

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if i==0 and j>0: 
                    dp[i][j] = dp[i][j-1] + grid[i][j] 
                    continue
                if j==0 and i>0: 
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                    continue
                if i>0 and j>0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                else:
                    dp[i][j] = grid[i][j]
        return dp[r-1][c-1]               
# @lc code=end

Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]])