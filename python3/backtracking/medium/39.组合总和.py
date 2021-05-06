#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

from typing import List

# @lc code=start
class Solution:

    def backtrack(self, candidates: List[int], target: int, index: int, combination: List[int], ans: List[List[int]]):
        if sum(combination)==target and combination not in ans:
            ans.append(combination.copy())
            return
        for i in range(index, len(candidates)):
            # 连续相同数剪枝
            if candidates[i]==candidates[i-1] and i > 0:
                continue
            # 大于目标值剪枝
            if sum(combination) >= target:
                return
            # 当前和+下一个数>target剪枝
            if sum(combination) + candidates[i] > target:
                return
            # 数可重复用i不需要+1
            combination.append(candidates[i])
            self.backtrack(candidates, target, i, combination, ans)
            combination.remove(candidates[i])

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or target==0: return None
        ans = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], ans)
        return ans
# @lc code=end

Solution().combinationSum([2,3,6,7], 7)