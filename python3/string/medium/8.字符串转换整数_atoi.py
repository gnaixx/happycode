#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    # 根据三种状态决定下一步逻辑
    BEGIN, PM, CONTINUE, STOP = 0, 1, 2, 100
    def check(self, c: str, state:int, num: int, pm: int) -> int:
        if c == ' ' and state == self.BEGIN:
            return self.BEGIN, num, pm

        if c in ['-','+'] and state == self.BEGIN:
            pm = -1 if c=='-' else 1
            return self.PM, num, pm

        if c.isdigit():
            newNum = num * 10 + int(c) * pm
            if newNum<=2**31-1 and newNum>=-2**31:
                num = newNum
                return self.CONTINUE, num, pm
            else:
                num = 2**31-1 if pm==1 else -2**31
                return self.STOP, num, pm

        if not c.isdigit():
            return self.STOP, num, pm


    def myAtoi(self, s: str) -> int:
        state, num, pm= 0, 0, 1
        for i in range(len(s)):
            state, num, pm = self.check(s[i], state, num, pm)
            if state == self.STOP:
                break
        return num
# @lc code=end

print(Solution().myAtoi('21474836460'))