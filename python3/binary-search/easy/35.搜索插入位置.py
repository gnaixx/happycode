#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

from typing import List

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = int((end + start)/2)
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start
# @lc code=end

Solution().searchInsert([1,3,5,6], 5)