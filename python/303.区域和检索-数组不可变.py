#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:
    def __init__(self, nums: List[int]):
        self.sum = [0] * len(nums)
        if len(nums) == 0:
           return
        for i in range(len(nums)):
            self.sum[i] = self.sum[i-1] + nums[i] if i > 0 else nums[i]


    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sum[j]
        return self.sum[j] - self.sum[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

