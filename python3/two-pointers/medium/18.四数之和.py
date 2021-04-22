#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

from typing import List

# @lc code=start
class Solution:
    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
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
    
    def backtrack(self, nums: List[int], target: int, size: int, index: int, combination: List[int], ans: List[List[int]]):
        cSize, cSum = len(combination), sum(combination)
        if cSize==size and cSum==target:
            ans.append(combination.copy())
            return
        for i in range(index, len(nums)):
            # 长度不足
            if len(nums)-i < size - cSize:
                return
            # 连续相同
            if nums[i]==nums[i-1] and i > index:
                continue
            # 之前总和+当前数+下个数*(剩余个数) > 目标值
            if i<len(nums)-1 and cSum + nums[i] + nums[i+1]*(size-cSize-1) > target:
                return
            # 之前总和+当前数+最后一个数*(剩余个数) < 目标值
            if cSum + nums[i] + nums[len(nums)-1]*(size-cSize-1) < target:
                continue
            combination.append(nums[i])
            self.backtrack(nums, target, size, i+1, combination, ans)
            combination.remove(nums[i])

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4: return []
        nums.sort()
        ans = []
        self.backtrack(nums, target, 4, 0, [], ans)
        return ans

# @lc code=end

Solution().fourSum([-3,-1,0,2,4,5], 0)