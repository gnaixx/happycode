#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    # 动态规划: dp[i] = min(dp[i], dp[i-j*j] + 1)
    # 测试数据比较大，按注释部分会超时
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0], dp[1] = 0, 1
        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                # if j*j == i: 
                #     dp[i] = 1
                #     break
                # dp[i] = min(dp[i], dp[j*j] + dp[i-j*j])
                dp[i] = min(dp[i], dp[i-j*j] + 1)
                j += 1
        return dp[n]
# @lc code=end

print(Solution().numSquares(6616))

