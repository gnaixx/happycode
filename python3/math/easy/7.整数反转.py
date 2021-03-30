#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if (x < 0):
            string = str(0-x)
            expect = 0 - int(string[::-1])
        else:
            string = str(x)
            expect = int(string[::-1])
            
        return expect if -2**31<expect and expect < 2**31-1 else 0

# @lc code=end

print(Solution().reverse(1534236469))