#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

from typing import List

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0]==1: return 0
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        for i in range(0, len(obstacleGrid)):
            for j in range(0, len(obstacleGrid[i])):
                # 判断第一行第一列是否能走到
                if i==0 and 1 not in obstacleGrid[0][0:j]: dp[i][j]=1
                if j==0 and 1 not in list(zip(*obstacleGrid))[0][0:i+1]: dp[i][j]=1
                if obstacleGrid[i][j]==1: 
                    dp[i][j] = 0
                elif i>0 and j>0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[i][j]
# @lc code=end

Solution().uniquePathsWithObstacles([[0,0],[1, 1], [0,0]])
Solution().uniquePathsWithObstacles([[1, 0]])
Solution().uniquePathsWithObstacles([[0, 1]])
Solution().uniquePathsWithObstacles([[0,0],[0,1]])
Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])