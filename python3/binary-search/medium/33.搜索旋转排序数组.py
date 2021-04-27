#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

from typing import List

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            # 前半段符合正序, mid可能为0
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # 后半段符合正序
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
# @lc code=end

Solution().search( [3,1], 1)