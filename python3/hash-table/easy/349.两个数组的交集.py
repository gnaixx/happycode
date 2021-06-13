#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            if i in nums2 and i not in ans:
                ans.append(i)
        return ans
# @lc code=end

