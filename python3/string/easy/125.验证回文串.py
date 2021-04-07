#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x1 = ''.join(list(filter(str.isalnum, s.lower())))
        return x1 == x1[::-1]
# @lc code=end

Solution().isPalindrome('race a car')
