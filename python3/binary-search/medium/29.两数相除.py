#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def div(self, dividend: int, divisor: int) -> int:
        # 除数小于or等于被除数特殊处理
        if dividend < divisor: return 0
        if dividend == divisor: return 1
        # 找出除数翻倍情况下大于被除数的count数
        sum, count = divisor, 1
        while dividend >= sum:
            sum, count = sum<<1, count<<1
        sum, count = sum>>1, count>>1
        # 找出最大的小于被除数翻倍数，进行递归
        return count + self.div(dividend-sum, divisor)

    def divide(self, dividend: int, divisor: int) -> int:
        if divisor==1: return dividend
        # 最大值为int32
        if divisor==-1 and dividend==-2**31:
            return 2**31-1
        # 全部转为正数计算
        if dividend>0 and divisor>0:
            return self.div(dividend, divisor)
        elif dividend>0 or divisor>0:
            return -self.div(abs(dividend), abs(divisor))
        else:
            return self.div(abs(dividend), abs(divisor))
# @lc code=end

Solution().divide(-2147483648, -1)
