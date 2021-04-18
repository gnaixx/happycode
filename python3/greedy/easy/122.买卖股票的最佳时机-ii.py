#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    # 动态规划 dp0前一天没股票 dp1前一天有股票
    def maxProfit(self, prices: List[int]) -> int:
        dp0, dp1= 0, -prices[0]
        for i in range(1, range(len(prices))):
            newDp0 = max(dp0, dp1 + prices[i])
            newDp1 = max(dp1, dp0 - prices[i])
            dp0 = newDp0
            dp1 = newDp1
        return dp0
    
    # 贪心算法
    # def maxProfit(self, prices: List[int]) -> int:
    #     maxProfit = 0
    #     ans = 0
    #     for i in range(1, len(prices)):
    #         ans += max(0, prices[i]-prices[i-1])
    #     return ans
# @lc code=end

