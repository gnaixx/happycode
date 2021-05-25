#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        # bin, ans = [], 0
        # for i in range(32):
        #     bin.append(n>>i & 0x01)
        # for i in range(32):
        #     ans = ans<<1 | bin[i]
        # return ans
        oribin = '{0:032b}'.format(n)
        tarbin = oribin[::-1]
        return int(tarbin, 2)
# @lc code=end

Solution().reverseBits(43261596)