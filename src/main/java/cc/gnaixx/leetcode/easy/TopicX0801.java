package cc.gnaixx.leetcode.easy;

import cc.gnaixx.leetcode.tool.LogT;

/**
 * name: TopicX0801
 * desc: 三步问题
 *
 * @author: xiangqing
 * @date: 2020/05/09
 */
public class TopicX0801 {
    public int waysToStep(int n) {
        int[] dp = new int[n + 3];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        for (int i = 4; i <= n; i++) {
            dp[i] = (dp[i - 1] + dp[i - 2]) %  1000000007 + dp[i - 3]; // 前两个相加可能溢出
            dp[i] %= 1000000007;
        }
        return dp[n];
    }

    public static void main(String[] args) {
        LogT.print(new TopicX0801().waysToStep(3));
        LogT.print(new TopicX0801().waysToStep(5));
    }
}
