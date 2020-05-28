#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    # 动态规划
    # 计算前一步最大值加上当前值和当前值对比
    # 如果当前值更大，则以当前值为启动
    def maxSubArray(self, nums: List[int]) -> int:
        preSum = maxSum = nums[0]
        for num in nums[1:]:
            preSum = max(preSum + num, num)
            maxSum = max(preSum, maxSum)
        return maxSum

    # 动态规划
    # 前一步最大值如果为正数则加上当前值为最大
    # 判断前一步最大值加上当前值的大小
    # def maxSubArray(self, nums: List[int]) -> int:
    #     sum, maxSum = 0, nums[0]
    #     for num in nums:
    #         sum = sum+num if sum > 0 else num
    #         maxSum = max(maxSum, sum)
    #     return maxSum
# @lc code=end

