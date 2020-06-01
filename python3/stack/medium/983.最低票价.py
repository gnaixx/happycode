#
# @lc app=leetcode.cn id=983 lang=python3
#
# [983] 最低票价
#

# @lc code=start
class Solution:
    # dp 算法, 计算当天买票花销最优解，无旅行计划则按照最近前一次花费
    # dp[i] = min(dp[i-1]+dailyCosts, dp[i-7]+weeklyCosts, dp[i-30]+monthlyCosts)
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayCost = [0] * 366
        dayIndex = 0
        for i in range(1, 366):
            if dayIndex >= len(days):
                break
            if i != days[dayIndex]:
                dayCost[i] = dayCost[i-1]
                continue
            costDaily = dayCost[max(i-1, 0)] + costs[0]
            costWeekly = dayCost[max(i-7, 0)] + costs[1]
            costMonthly = dayCost[max(i-30, 0)] + costs[2]
            dayCost[i] = min(costDaily, costWeekly, costMonthly)
            dayIndex += 1
        return dayCost[days[dayIndex - 1]]
# @lc code=end

