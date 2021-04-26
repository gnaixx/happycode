#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

from typing import List

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从后找出nums[i]<nums[i+1], i后数组为倒序
        i = len(nums)-2
        while i>=0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            # 从后(i,n]找出第一个比 nums[i] 大的数
            j = len(nums)-1
            while j > i and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # 正排i后数组
        l, r = i+1, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return 
# @lc code=end

Solution().nextPermutation([4,5,2,6,4,3,1])

