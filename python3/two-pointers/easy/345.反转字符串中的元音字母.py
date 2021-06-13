#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def isVowel(self, c: str) -> bool:
        return c.lower() in ['a', 'e', 'o', 'i', 'u']
        
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s)-1
        ss = list(s)
        while l < r:
            if not self.isVowel(s[l]):
                l += 1
            elif not self.isVowel(s[r]):
                r -= 1
            else:
                ss[l], ss[r] = ss[r], ss[l]
                l, r = l+1, r-1
        return ''.join(ss)
# @lc code=end

