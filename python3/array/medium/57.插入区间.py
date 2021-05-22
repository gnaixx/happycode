#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

from typing import List

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e, ans = newInterval[0], newInterval[1], []
        for val in intervals:
            # 找出最大新增区间
            if val[0]<=s<=val[1] or val[0]<=e<=val[1]:
                s = min(val[0], s)
                e = max(val[1], e)
            # 包含在区间内忽略
            if s<=val[0] and val[1]<=e:
                continue
            # 由于按起始断点排序
            if e<val[0] and [s, e] not in ans:
                ans.append([s, e])
            ans.append(val)
        if [s, e] not in ans: ans.append([s, e])
        return ans
# @lc code=end

# Solution().insert([[1,3],[6,9]], [2,5])
# Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
# Solution().insert([], [5,7])
# Solution().insert([[1,5]], [2,3])
# Solution().insert([[1,5]], [2,7])
Solution().insert([[2,5],[6,7],[8,9]], [0,1])

