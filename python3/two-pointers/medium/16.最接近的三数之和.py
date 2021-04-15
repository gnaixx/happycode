#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

from typing import List

# @lc code=start
class Solution:
    # 定位一个数后找出每轮最优解
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            s, e = i+1, len(nums)-1
            while s < e:
                tmp = nums[i] + nums[s] + nums[e]
                if tmp == target:
                    return target
                if tmp < target:
                    ss = nums[s]
                    while s < e and nums[s] == ss:
                        s += 1
                if tmp > target:
                    ee = nums[e]
                    while s < e and nums[e] == ee:
                        e -= 1
                ans = tmp if abs(target-tmp) < abs(target-ans) else ans
        return ans
# @lc code=end

Solution().threeSumClosest([0,1,2], 0)
