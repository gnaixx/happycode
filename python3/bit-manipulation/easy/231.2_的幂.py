#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if not n: return False
        # while n:
        #     if n==1: return True
        #     if n % 2: return False
        #     n >>= 1
        # return True
        return (n>0) and (n&(n-1))==0
# @lc code=end

Solution().isPowerOfTwo(0)