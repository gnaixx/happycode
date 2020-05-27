#
# @lc app=leetcode.cn id=877 lang=python3
#
# [877] 石子游戏
#

from typing import List

# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        total = 0
        i, j = 0, len(piles)-1
        dp0, dp1 = 0, 0
        while(i<j):
            total += piles[i] + piles[j]
            dp0 += piles[i] if piles[i] > piles[j] else piles[j]
            i += 1
            j -= 1
        return dp0 > total - dp0 
# @lc code=end

Solution().stoneGame([5, 3, 4, 5])

