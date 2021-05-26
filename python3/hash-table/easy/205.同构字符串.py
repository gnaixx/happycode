#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        bitA, bitB = {}, {}
        for i in range(len(s)):
            cs, ct = s[i], t[i]
            if cs not in bitA.keys() and ct not in bitB.keys():
                bitA[cs], bitB[ct] = i, i
            elif cs in bitA.keys() and ct in bitB.keys():
                if bitA[cs] != bitB[ct]: return False
            else:
                return False
        return True
# @lc code=end

Solution().isIsomorphic('bbbaaaba', 'aaabbbba')