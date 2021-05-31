#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    # n=2^a + 3^b + 5^c
    def isUgly(self, n: int) -> bool:
        if n<=0: return False
        for i in [2, 3, 5]:
            while n%i==0:
                n //= i
        return n==1
# @lc code=end

