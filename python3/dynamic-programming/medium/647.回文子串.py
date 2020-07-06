#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        length = len(s)
        dp = [[False] * length for _ in range(length)]
        for l in range(length):
            for i in range(length):
                j = i + l
                if j >= length: break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                count += 1 if dp[i][j] else 0
        return count
        
# @lc code=end

