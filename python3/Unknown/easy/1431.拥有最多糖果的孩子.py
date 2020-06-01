#
# @lc app=leetcode.cn id=1431 lang=python3
#
# [1431] 拥有最多糖果的孩子
#

# @lc code=start
class Solution:
    # 找出最大值
    # 当前点加上额外的是否大于等于最大值
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False] * len(candies)
        maxNum = max(candies)
        for i in range(len(candies)):
            if candies[i] == maxNum:
                res[i] = True
                continue
            res[i] = candies[i] + extraCandies >= maxNum
        return res
# @lc code=end

