package cc.gnaixx.leetcode.medium;

import cc.gnaixx.leetcode.Log;

/**
 * name: Topic983
 * desc: 最低票价
 *
 * @author xiangqing.xxq
 * @date 2020/05/06
 */
public class Topic983 {

    // dp 算法, 计算当天买票花销最优解，无旅行计划则按照最近前一次花费
    // dp[i] = min(dp[i-1]+dailyCosts, dp[i-7]+weeklyCosts, dp[i-30]+monthlyCosts)
    public int mincostTickets(int[] days, int[] costs) {
        int[] dayCost = new int[366];

        int dayIndex = 0;
        for (int i = 1; i <= 365 && dayIndex < days.length; i++) {
            if (i != days[dayIndex]) {
                dayCost[i] = dayCost[i - 1];
                continue;
            }
            int costDaily = dayCost[Math.max(i - 1, 0)] + costs[0];
            int costWeekly = dayCost[Math.max(i - 7, 0)] + costs[1];
            int costMonthly = dayCost[Math.max(i - 30, 0)] + costs[2];
            dayCost[i] = Math.min(Math.min(costDaily, costWeekly), costMonthly);
            dayIndex++;
        }
        return dayCost[days[dayIndex - 1]];
    }

    public static void main(String args[]) {
        Log.print(new Topic983().mincostTickets(
                new int[]{1, 4, 6, 7, 8, 20},
                new int[]{2, 7, 15}
        ));

        Log.print(new Topic983().mincostTickets(
                new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31},
                new int[]{2, 7, 15}
        ));

        Log.print(new Topic983().mincostTickets(
                new int[]{1, 4, 6, 7, 8, 9, 10, 13, 14, 15, 16, 20},
                new int[]{2, 7, 15}
        ));
    }
}
