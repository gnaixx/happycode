#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i]==' ' and count!=0: break
            if s[i]==' ': continue
            count += 1
        return count
# @lc code=end

Solution().lengthOfLastWord('b    a    ')