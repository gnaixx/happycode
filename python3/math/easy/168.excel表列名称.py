#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber:
            ans = chr((columnNumber-1) % 26 + ord('A')) + ans
            columnNumber = (columnNumber-1) // 26
        return ans
# @lc code=end

Solution().convertToTitle(701)