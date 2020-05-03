package cc.gnaixx.leetcode.easy;

/**
 * name: Topic53
 * desc: 最大子序和-动态规划
 *
 * @author: xiangqing
 * @date: 2020/05/03
 */
public class Topic53 {
    public int maxSubArray(int[] nums) {
        int max = nums[0];
        int pre = nums[0];
        for (int i=1; i<nums.length; i++) {
            pre = (pre + nums[i]) > nums[i] ? pre + nums[i] : nums[i];
            max = pre > max ? pre : max;
        }
        return max;
    }

    public static void main(String[] args) {
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int max = new Topic53().maxSubArray(nums);
        System.out.println(max);
    }
}
