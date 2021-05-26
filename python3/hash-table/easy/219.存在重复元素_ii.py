#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

from typing import List

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i in range(len(nums)):
            if nums[i] in map.keys() and abs(i-map[nums[i]])<=k:
                return True
            else:
                map[nums[i]] = i
        return False
# @lc code=end

Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2)