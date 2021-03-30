#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        KV = {'(':')', '{':'}', '[':']'}
        stack = [s[0]]
        for i in range(1,len(s)):
            if len(stack)==0:
                stack.append(s[i])
                continue
            x = stack.pop()
            if x not in KV.keys() or KV[x] != s[i]:
                stack.append(x)
                stack.append(s[i])
        return len(stack) == 0

# @lc code=end

print(Solution().isValid('([)]'))
