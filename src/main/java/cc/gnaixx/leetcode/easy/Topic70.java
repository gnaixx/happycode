package cc.gnaixx.leetcode.easy;

import cc.gnaixx.leetcode.tool.LogT;

/**
 * name: Topic70
 * desc:
 *
 * @author: xiangqing
 * @date: 2020/05/11
 */
public class Topic70 {

    public int climbStairs(int n) {
        int[] dp = new int[n + 2];
        dp[1] = 1;
        dp[2] = 2;

        for (int i=3; i<=n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }


    public static void main(String[] args) {
        LogT.print(new Topic70().climbStairs(3));
        LogT.print(new Topic70().climbStairs(2));
    }
}
