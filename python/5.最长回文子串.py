#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:

    # 中心扩展，单前字符串往周边扩展
    # 情况1, aba 形式
    # 情况2, abba 形式
    # def longestPalindrome(self, s: str) -> str:
    #     if not s:
    #         return s

    #     sLen = len(s)
    #     ret = s[0]
    #     for i, c in enumerate(s):
    #         spread = 1
    #         while(i-spread>=0 and i+spread<sLen) and s[i-spread] == s[i+spread]:
    #             if spread*2+1 > len(ret):
    #                 ret = s[i-spread: i+spread+1]
    #             spread += 1

    #         spread = 1
    #         while( i-spread+1>=0 and i+spread<sLen) and s[i-spread+1] == s[i+spread]:
    #             if spread*2 > len(ret):
    #                 ret = s[i-spread+1: i+spread+1]
    #             spread += 1
    #     return ret

    # 动态规划
    # l 表示回文长度
    # 当子串为回文是头尾两个字符必须一样
    # P(i,j)=P(i+1,j−1)∧(Si==Sj)
    def longestPalindrome(self, s: str) -> str:
        ret = ''
        sLen = len(s)
        dp = [[False] * sLen for _ in range(sLen)]
        for l in range(sLen):
            for i in range(sLen):
                j = i+l
                if j >= sLen: break

                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i]==s[j] and dp[i+1][j-1]
                
                if dp[i][j] and l+1 > len(ret):
                    ret = s[i:j+1]
        return ret
# @lc code=end

ret = Solution().longestPalindrome('aaabaaaa')
print(ret)

