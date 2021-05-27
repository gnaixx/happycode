#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

from typing import List

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        s, e, ans = nums[0], nums[0], []
        for i in range(1, len(nums)):
            if nums[i]-1 > e: 
                ans.append(str(s) if s==e else ('%d->%d' % (s, e)))
                s, e = nums[i], nums[i]
            else:
                e = nums[i]
        ans.append(str(s) if s==e else ('%d->%d' % (s, e)))
        return ans
# @lc code=end

Solution().summaryRanges([-1])
Solution().summaryRanges([0,2,3,4,6,8,9])
# Solution().summaryRanges([0,1,2,4,5,7])