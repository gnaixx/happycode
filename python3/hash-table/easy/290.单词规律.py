#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash1, hash2 = [], []
        for i, _ in enumerate(pattern):
            hash1.append(pattern.find(pattern[i]))
        sList = s.split()
        for i, v in enumerate(sList):
            hash2.append(sList.index(v))
        return hash1 == hash2
# @lc code=end

Solution().wordPattern('abba', 'dog cat cat dog')