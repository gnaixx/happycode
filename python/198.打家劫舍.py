#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        preMax = 0
        curMax = 0
        for num in nums:
            tmp = curMax
            curMax = max(preMax+num, curMax)
            preMax = tmp
        return curMax

# @lc code=end

