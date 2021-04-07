#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        array = filter(str.isalnum, s)
        x1 = ''.join(list(array))
        x2 = x1[::-1]
        return x1 == x2
# @lc code=end

Solution().isPalindrome('race a car')
