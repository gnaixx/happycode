#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

from typing import List

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
# @lc code=end
Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])