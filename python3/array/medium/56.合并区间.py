#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

from typing import List

# @lc code=start
class Solution:
    def sortStart(self, intervals: List[List[int]]) -> List[List[int]]:
        dict, list = {}, []
        for i, v in enumerate(intervals):
            dict[v[0]] = v
        for i in sorted(dict):
            list.append(dict[i])
        return list

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in sorted(intervals, key=lambda i:i[0]):
            if ans and i[0] <= ans[-1][1]:
                ans[-1][1] = max(i[1], ans[-1][1])
            else:
                ans.append(i)
        return ans
# @lc code=end

# Solution().merge([[2,6],[1,3],[8,10],[15,18]])
# Solution().merge([[1,4],[5,6]])
Solution().merge([[1,4],[2,3]])