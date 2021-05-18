#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for c in columnTitle:
            ans = ord(c)-ord('A')+1 + ans*26
        return ans
# @lc code=end

Solution().titleToNumber('ZY')