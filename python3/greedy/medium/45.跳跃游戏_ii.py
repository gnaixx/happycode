#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
from typing import List


class Solution:
    # 反向查找能到达单前位置的点
    def jump2(self, nums: List[int]) -> int:
        position = len(nums) - 1
        step = 0
        while position:
            for i in range(position):
                if i+nums[i] >= position:
                    position = i
                    step += 1
                    break
        return step

    # 找出当前边界能跳跃的最大值
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
# @lc code=end

Solution().jump([2,3,1,1,4])