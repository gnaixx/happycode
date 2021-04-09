#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

from typing import List

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maxLen, currStr, currLen, i = 0, {}, 0, 0
        # while i < len(s):
        #     if s[i] not in currStr.keys():
        #         currLen += 1
        #         currStr[s[i]] = i
        #     else:
        #         i = currStr[s[i]] + 1
        #         currLen = 1
        #         currStr.clear()
        #         currStr[s[i]] = i
        #     i += 1
        #     maxLen = max(currLen, maxLen)
        # return maxLen
        start, maxLen, useChar = 0, 0, {}
        for i in range(len(s)):
            if s[i] in useChar and start <= useChar[s[i]]:
                start = useChar[s[i]] + 1
            else:
                maxLen = max(maxLen, i - start + 1)
            useChar[s[i]] = i
        return maxLen
# @lc code=end

Solution().lengthOfLongestSubstring('abcabcbb')