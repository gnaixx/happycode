#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        # while n != 1:
        #     s = str(n)
        #     sum = 0
        #     for i in range(0, len(s)):
        #         sum += int(s[i])*int(s[i])
        #     n = sum
        #     if n>=2 and n <=9:
        #         return False
        # return True
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1
# @lc code=end

Solution().isHappy(1111111)
