#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
from typing import List


class Solution:
    def backtrack(self, nums: List[int], combination:List[int], ans:List[List[int]]):
        if len(combination)==len(nums) and combination not in ans:
            ans.append(combination.copy())
            return
        for i in range(len(nums)):
            if nums[i] in combination:
                continue
            combination.append(nums[i])
            self.backtrack(nums, combination, ans)
            combination.remove(nums[i])

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack(nums, [], ans)
        return ans
# @lc code=end

Solution().permute([1,2,3])
