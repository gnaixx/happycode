#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:

    # 存储之前最大值，及单前最大值
    # def rob(self, nums: List[int]) -> int:
    #     preMax = 0
    #     curMax = 0
    #     for num in nums:
    #         tmp = curMax
    #         curMax = max(preMax+num, curMax)
    #         preMax = tmp
    #     return curMax

    # dp0 表示单前节点不偷，所以最大值可以为前一个节点偷or不偷
    # dp1 表示单前节点偷，必须前一个节点为不偷
    # 比较最终 max(dp0, dp1)
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp0 = 0
        dp1 = nums[0]
        for i in range(1, len(nums)):
            tmp0 = max(dp0, dp1)
            tmp1 = dp0 + nums[i]
            dp0, dp1 = tmp0, tmp1
        return max(dp0, dp1)

# @lc code=end

