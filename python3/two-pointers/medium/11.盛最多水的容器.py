#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

from typing import List

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, ans = 0, len(height)-1, 0
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l+=1 
            else:
                r-=1
        return ans
# @lc code=end

Solution().maxArea([1,8,6,2,5,4,8,3,7])