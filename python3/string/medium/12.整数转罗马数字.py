#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        K = [1000, 500, 100, 50, 10, 5, 1]
        V = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        ans, index = '', 0
        while num:
            while index < len(K):
                if num >= K[index]:
                    ans += V[index]
                    num -= K[index]
                    break
                else:
                    index += 1
        ans = ans.replace('DCCCC', 'CM').replace('CCCC', 'CD')
        ans = ans.replace('LXXXX', 'XC').replace('XXXX', 'XL')
        ans = ans.replace('VIIII', 'IX').replace('IIII', 'IV')
        return ans
# @lc code=end

Solution().intToRoman(9)