#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

from typing import List

# @lc code=start
class Solution:
    def backtrack(self, ans:List[str], combination:str, l:int, r:int, n:int):
        if l==n and r==n:
            ans.append(combination)
            return
        if l < n:
            combination += '('
            self.backtrack(ans, combination, l+1, r, n)
            combination = combination[:-1]
        # r<l 保证括号有效
        if r < l:
            combination += ')'
            self.backtrack(ans, combination, l, r+1, n)
            combination = combination[:-1]

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.backtrack(ans, '', 0, 0, n)
        return ans
# @lc code=end

Solution().generateParenthesis(2)