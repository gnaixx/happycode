#
# @lc app=leetcode.cn id=967 lang=python3
#
# [967] 连续差相同的数字
#

from typing import List
# @lc code=start
class Solution:
    
    # 动态规划
    # 计算满足差值的少一个位数的全部值，在满足条件下添加一位
    # dp(n) = dp(n-1) + sum(num%10+K<=9 || num%10-K>=0)
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        nums = set(range(1, 10))
        for _ in range(N - 1):
            tmpNums = set()
            for num in nums:
                n1 = num % 10
                if n1 + K <= 9:
                    tmpNums.add(num * 10 + n1 + K)
                if n1 - K >= 0:
                    tmpNums.add(num * 10 + n1 - K)
            nums = tmpNums

        if N == 1:
            nums.add(0)
        return list(nums)
        
# @lc code=end

print(Solution().numsSameConsecDiff(4, 4))

