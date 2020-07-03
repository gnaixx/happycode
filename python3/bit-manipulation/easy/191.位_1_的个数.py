#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    # def hammingWeight(self, n: int) -> int:
    #     return str(bin(n)).count('1')

    # 依次去除从右往左的第一个1
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += 1
            n &= n-1
        return count
        
# @lc code=end

