#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#
from typing import List

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        value = [0] * 101
        for height in heights:
            value[height] += 1
        j = 0
        count = 0
        for i in range(len(value)):
            while value[i] > 0:
                value[i] -= 1
                if (heights[j] != i): count += 1
                j += 1
        return count

# @lc code=end

Solution().heightChecker([1,1,4,2,1,3])

