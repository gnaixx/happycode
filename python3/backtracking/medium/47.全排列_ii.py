#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
from typing import List


class Solution:
    def backtrack(self, nums: List[int], combination:List[int], ans:List[List[int]]):
        if 0==len(nums) and combination not in ans:
            ans.append(combination.copy())
            return
        for i in range(len(nums)):
            combination.append(nums[i])
            self.backtrack(nums[:i]+nums[i+1:], combination, ans)
            # 不能用remove方法会导致第一个重复整数被删除
            combination.pop()        

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack(nums, [], ans)
        return ans
# @lc code=end

Solution().permuteUnique([2,2,1,1])