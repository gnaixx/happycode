#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    # 第一个阶梯有一种可能，第二个为2
    # 后续到达目标阶梯前都有两个选择
    # 选择跨一步或者两步
    # dp[i-1] + dp[i+2] 就位当前可能步数
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 2)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
# @lc code=end

