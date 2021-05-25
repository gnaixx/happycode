#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zcount = 0
        while n:
            n //= 5
            zcount += n
        return zcount
# @lc code=end

