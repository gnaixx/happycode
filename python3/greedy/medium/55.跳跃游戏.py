#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

from typing import List

# @lc code=start
class Solution:
    def canJump2(self, nums: List[int]) -> bool:
        position, step, reach = len(nums)-1, 0, False
        while position:
            reach = False
            # 从后开始找减少耗时
            for i in range(position-1, -1, -1):
                if i+nums[i] >= position:
                    step, position, reach = step+1, i, True
                    break
            # 如果遍历后找不到能达到当前点，直接返回
            if not reach: break
        return position==0 

    def canJump(self, nums: List[int]) -> bool:
        maxPosition = 0
        for i, n in enumerate(nums):
            # 单前节点超过能达到最大节点则失败
            if i > maxPosition:
                return False
            maxPosition = max(maxPosition, i+n)
        return True
# @lc code=end

Solution().canJump([1, 0, 1,0])