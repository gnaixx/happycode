#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

from typing import List

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(i) for i in str(int(''.join([str(i) for i in digits])) + 1)]
# @lc code=end

Solution().plusOne([1,9,9])
