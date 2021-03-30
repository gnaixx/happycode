#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

from typing import List

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        if len(nums)==1: return 1

        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index += 1
        return index
# @lc code=end

Solution().removeDuplicates([1,1,2])