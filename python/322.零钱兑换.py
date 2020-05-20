#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

from typing import List

# @lc code=start
class Solution:
    # 动态规划
    # 计算总额减去可用领取后最小值
    # fn = min{f(n-k1), f(n-k2) ..., f(n-kn)}
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: 
            return 0

        dp = [float('inf')] * (amount+1)
        for index in range(amount + 1):
            currMin = float('inf')
            for coin in coins:
                if index - coin > 0:
                    currMin = min(dp[index - coin]+1, currMin)
                if index == coin:
                    currMin = 1
            dp[index] = currMin
                
        return -1 if dp[amount] == float('inf') else dp[amount]

# @lc code=end

print(Solution().coinChange([2,5,10], 27))

