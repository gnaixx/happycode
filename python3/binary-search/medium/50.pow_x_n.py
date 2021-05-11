#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    # 递归
    def myPow2(self, x: float, n: int) -> float:
        if not n: return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

    # 迭代
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1/x, -n
        pow = 1
        while n:
            if n % 2:
                pow *= x
            x, n = x*x, int(n/2)
        return pow
# @lc code=end

Solution().myPow(2.000, 10)