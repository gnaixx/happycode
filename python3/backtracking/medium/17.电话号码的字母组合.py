#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

from typing import List

# @lc code=start
class Solution:
    ans = []
    table = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def backtrack(self, combination: str, digits: str):
        if not digits: 
            self.ans.append(combination)
            return
        for c in self.table[int(digits[0])]:
            self.backtrack(combination + c, digits[1:])

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return [] 
        self.ans = []
        self.backtrack('', digits)
        return self.ans
# @lc code=end

Solution().letterCombinations('2')