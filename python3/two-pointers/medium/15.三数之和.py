#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

from typing import List

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 排序
        nums.sort()
        list = []
        for i in range(len(nums)):
            # 重复数直接过滤
            if i>0 and nums[i]==nums[i-1]:
                continue
            # 查找剩余数相加是否等于0
            s, e = i+1, len(nums)-1
            while s < e:
                sum = nums[i] + nums[s] + nums[e]
                # 等于0加入, 需要继续查找
                if sum == 0:
                    ans = [nums[i], nums[s], nums[e]]
                    if ans not in list:
                        list.append(ans)
                    s += 1
                # 向右查找，过滤重复数
                if sum < 0:
                    ss = nums[s]
                    while s < e and ss==nums[s]:
                        s += 1
                # 向左查找，过滤重复数
                if sum > 0:
                    ee = nums[e]
                    while s < e and ee==nums[e]:
                        e -= 1
        return list
# @lc code=end

Solution().threeSum([-1,0,1,2,-1,-4])