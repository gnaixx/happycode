#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        start, end, ans = 0, x, 0
        while start <= end:
            mid = int((start + end) / 2)
            if mid*mid <= x:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        return ans
# @lc code=end

Solution().mySqrt(1)
