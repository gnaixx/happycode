#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        ans = 0
        pointer = [1 for _ in range(n)]
        for i in range(2, n):
            if pointer[i] == 1:
                ans += 1
                # i 为质数则i的倍数非质数
                if (i*i < n):
                    for j in range(i*i, n , i):
                        pointer[j] = 0
        return ans
# @lc code=end

