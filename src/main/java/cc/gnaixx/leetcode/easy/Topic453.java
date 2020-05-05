package cc.gnaixx.leetcode.easy;

/**
 * name: Topic453
 * desc: 最小移动次数使数组元素相等
 *
 * @author: xiangqing
 * @date: 2020/05/03
 */
public class Topic453 {

    // 计算公式
    // sum + m(n-1) = xn   sum 为原始数组和，m 为移动步骤，n 为数组大小，x 为最后的相等值
    // m = x - min         移动次数为 x 和 原始数组最小值的差
    // m = sum - (min * n)
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
