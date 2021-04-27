#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

from typing import List

# @lc code=start
class Solution:
    def binarySearch(self, nums: List[int], target: int, isLeft: bool) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target or (not isLeft and nums[mid]==target):
                l = mid + 1
            else:
                r = mid - 1
        return l if isLeft else r
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = self.binarySearch(nums, target, True), self.binarySearch(nums, target, False)
        return [l, r] if l <= r else [-1, -1]

    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     if not nums: return [-1, -1]
    #     l, r, s, e = 0, len(nums)-1, -1, -1
    #     while l <= r:
    #         mid = (l+r) // 2
    #         if nums[mid] == target:
    #             s, e = mid, mid
    #             while (s-1>=0 and nums[s-1]==target) or (e+1<len(nums) and nums[e+1]==target):
    #                 if s-1>=0 and nums[s-1]==target:
    #                     s -= 1
    #                 if e+1<len(nums) and nums[e+1]==target:
    #                     e += 1
    #             return [s, e]
    #         if nums[mid] < target:
    #             l = mid + 1
    #         else:
    #             r = mid - 1
    #     return [-1, -1]
# @lc code=end

Solution().searchRange([5,7,7,8,8,10], 8)