#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(n):
            sum = 0
            while  n > 0:
                n, digit = divmod(n, 10)
                sum += digit ** 2
            return sum
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            n = next_num(n)
        return n == 1
# @lc code=end

Solution().isHappy(7)
