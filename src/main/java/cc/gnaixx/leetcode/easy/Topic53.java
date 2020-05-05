package cc.gnaixx.leetcode.easy;

/**
 * name: Topic53
 * desc: 最大子序和-动态规划
 *
 * @author: xiangqing
 * @date: 2020/05/03
 */
public class Topic53 {

    // 先计算当前节点，再判断是否把单前节点加入
    public int maxSubArray(int[] nums) {
        int max = nums[0];
        int pre = nums[0];
        for (int i=1; i<nums.length; i++) {
            // pre = (pre + nums[i]) > nums[i] ? pre + nums[i] : nums[i];
            // max = pre > max ? pre : max;
            pre = Math.max(pre + nums[i], nums[i]);
            max = Math.max(pre, max);

        }
        return max;
    }

    // 先判断之前节点是否大于0
    public int maxSubArray2(int[] nums) {
        int sum = 0;
        int max = nums[0];
        for (int num : nums) {
            if (sum > 0) {
                sum += num;
            } else {
                sum = num;
            }
            max = Math.max(max, sum);
        }
        return max;
    }

    public static void main(String[] args) {
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int max = new Topic53().maxSubArray(nums);
        System.out.println(max);
    }
}
