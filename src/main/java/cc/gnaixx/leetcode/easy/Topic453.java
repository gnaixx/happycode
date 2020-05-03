package cc.gnaixx.leetcode.easy;

/**
 * name: Topic453
 * desc: sum + m(n-1) = xn; m = x - min -> sum - m
 *
 * @author: xiangqing
 * @date: 2020/05/03
 */
public class Topic453 {

    public int minMoves(int[] nums) {
        int min = nums[0];
        int sum = 0;
        for (int x : nums) {
            min = min > x ? x : min;
            sum += x;
        }
        return sum - (min * nums.length);
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        int length = new Topic453().minMoves(nums);
        System.out.println(length);
    }
}
