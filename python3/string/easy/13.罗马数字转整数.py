#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        KV = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ansers = KV[s[0]]
        for i in range(1, len(s)):
            if (s[i]=='V' or s[i]=='X') and s[i-1]=='I':
                ansers += KV[s[i]] - 2*KV[s[i-1]]
                continue
            if (s[i]=='L' or s[i]=='C') and s[i-1]=='X':
                ansers += KV[s[i]] - 2*KV[s[i-1]]
                continue
            if (s[i]=='D' or s[i]=='M') and s[i-1]=='C':
                ansers += KV[s[i]] - 2*KV[s[i-1]]
                continue
            ansers += KV[s[i]]
        return ansers
# @lc code=end

