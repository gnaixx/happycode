#
# @lc app=leetcode.cn id=17.16 lang=python3
#
# [17.16] 按摩师
#
from typing import List

# @lc code=start
class Solution:
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp0, dp1 = 0, nums[0]
        for i in range(1, n):
            tmp0 = max(dp0, dp1)
            tmp1 = dp0 + nums[i]
            dp0, dp1 = tmp0, tmp1
        return max(dp0, dp1)
            

# @lc code=end
