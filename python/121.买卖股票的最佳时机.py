#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
             return 0

        maxProfit = 0
        minPrice = prices[0]
        for price in prices:
            minPrice = minPrice if minPrice <= price else price
            maxProfit = (price - minPrice) if (price - minPrice) >= maxProfit else maxProfit
            
        return maxProfit

# @lc code=end
Solution().maxProfit([7,1,5])

