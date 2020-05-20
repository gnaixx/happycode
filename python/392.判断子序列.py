#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    
    # 直接按位对比
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        index = 0
        for c in t:
            if s[index] == c:
                index += 1
            if index == len(s):
                break
        return index == len(s)

# @lc code=end

