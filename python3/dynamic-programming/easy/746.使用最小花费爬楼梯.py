#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#
from typing import List

# @lc code=start
class Solution:

    # dp0 表示当前楼梯不爬，则前一个楼梯必须是爬过 dp1
    # dp1 表示当前楼梯要爬，则前一个楼梯可以是min(dp0, dp1) + cost[i]
    # 选择 dp0 dp1 最小值
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp0, dp1 = 0, cost[0]
        for i in range(1, len(cost)):
            tmp0 = dp1
            tmp1 = min(dp0, dp1) + cost[i]
            dp0, dp1 = tmp0, tmp1
        return min(dp0, dp1)
        
# @lc code=end

Solution().minCostClimbingStairs([0,0,1,1])

