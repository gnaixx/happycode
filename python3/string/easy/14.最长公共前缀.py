#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
from typing import List

# @lc code=start
class Solution:
    # 定一个子串, 从后往前缩减
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ''
        subString = strs[0]
        for s in strs:
            while not s.startswith(subString):
                subString = subString[0: -1]
        return subString
# @lc code=end

Solution().longestCommonPrefix(["flower","flow","flight"])

