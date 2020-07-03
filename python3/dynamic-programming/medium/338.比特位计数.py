#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#
from typing import List

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0, 1, 1]
        for i in range(3, num + 1):
            dp.append(dp[i>>1] + i%2)
        return dp[0:num+1]
        
# @lc code=end

Solution().countBits(5)
