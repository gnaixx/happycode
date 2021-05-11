#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

from typing import List

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return list(d.values())
# @lc code=end

Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])