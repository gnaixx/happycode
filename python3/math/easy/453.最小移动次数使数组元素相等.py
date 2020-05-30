#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小移动次数使数组元素相等
#

# @lc code=start
class Solution:
    # 计算公式
    # sum + m(n-1) = xn   sum 为原始数组和，m 为移动步骤，n 为数组大小，x 为最后的相等值
    # m = x - min         移动次数为 x 和 原始数组最小值的差
    # m = sum - (min * n)
    def minMoves(self, nums: List[int]) -> int:
        minNum, sumNum = min(nums), sum(nums)
        return sumNum - (minNum * len(nums))   
# @lc code=end

