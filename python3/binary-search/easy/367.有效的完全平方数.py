#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        s, e = 1, num // 2
        while s <= e:
            mid = (s + e) // 2
            tmp = mid * mid
            if tmp == num:
                return True
            if tmp > num: e = mid - 1 
            if tmp < num: s = mid + 1
        return False
# @lc code=end

Solution().isPerfectSquare(4)