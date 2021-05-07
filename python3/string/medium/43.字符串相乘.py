#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1, -1, -1):
            carry = 0
            for j in range(len(num2)-1, -1, -1):
                # 计算当前位结果，处理进位及余数
                tmp = (ord(num1[i])-ord('0')) * (ord(num2[j])-ord('0')) + carry
                carry = (ans[i+j+1]+tmp) // 10
                ans[i+j+1] = (ans[i+j+1]+tmp) % 10
            # 计算为倒排，每次计算后最高位为 i
            ans[i] += carry 
        ans = ''.join(map(str, ans))
        return '0' if not ans.lstrip('0') else ans.lstrip('0')
# @lc code=end

Solution().multiply('123', '456')