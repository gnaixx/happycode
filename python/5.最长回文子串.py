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
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s

        sLen = len(s)
        ret = s[0]
        for i, c in enumerate(s):
            spread = 1
            while(i-spread>=0 and i+spread<sLen) and s[i-spread] == s[i+spread]:
                if spread*2+1 > len(ret):
                    ret = s[i-spread: i+spread+1]
                spread += 1

            spread = 1
            while( i-spread+1>=0 and i+spread<sLen) and s[i-spread+1] == s[i+spread]:
                if spread*2 > len(ret):
                    ret = s[i-spread+1: i+spread+1]
                spread += 1
        return ret
# @lc code=end

ret = Solution().longestPalindrome('aaabaaaa')
print(ret)

