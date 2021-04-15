#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

from typing import List

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        list = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            s, e = i+1, len(nums)-1
            while s < e:
                sum = nums[i] + nums[s] + nums[e]
                if sum == 0:
                    ans = [nums[i], nums[s], nums[e]]
                    if ans not in list:
                        list.append(ans)
                    s += 1
                if sum < 0:
                    ss = nums[s]
                    while s < e and ss==nums[s]:
                        s += 1
                if sum > 0:
                    ee = nums[e]
                    while s < e and ee==nums[e]:
                        e -= 1
        return list
# @lc code=end

Solution().threeSum([-2,0,1,1,2])