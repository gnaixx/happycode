#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, l = len(haystack), len(needle)
        for start in range(n - l + 1):
            if haystack[start:start+l] == needle:
                return start
        return -1
# @lc code=end

Solution().strStr('hello', 'll')