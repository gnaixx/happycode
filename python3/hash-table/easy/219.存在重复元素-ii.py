#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

from typing import List

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
# @lc code=end

