#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
from typing import List

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
# @lc code=end

Solution().removeElement([0,1,2,2,3,0,4,2], 2)

