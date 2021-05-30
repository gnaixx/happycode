#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         return (lambda x:(x.sort(),x)[1])(list(s)) == (lambda x:(x.sort(),x)[1])(list(t))
# @lc code=end

Solution().isAnagram('rat', 'car')