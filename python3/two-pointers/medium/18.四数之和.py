#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

from typing import List

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 数组小于4 直接返回
        if len(nums) < 4:
            return []
        ans, n = [], len(nums)-1
        nums.sort()
        for i in range(n):
            # 重复数直接过滤
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, n):
                l, r = j+1, n
                while l < r:
                    sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum == target:
                        combination = [nums[i], nums[j], nums[l], nums[r]]
                        if combination not in ans:
                            ans.append(combination)
                        l += 1
                    if sum < target:
                        l += 1
                        while l < r and nums[l]==nums[l-1]:
                            l += 1
                    else:
                        r -= 1
                        while l < r and nums[r]==nums[r+1]:
                            r -= 1
        return ans
# @lc code=end

Solution().fourSum([-3,-1,0,2,4,5], 0)