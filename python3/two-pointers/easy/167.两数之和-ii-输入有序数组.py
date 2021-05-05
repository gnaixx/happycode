#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2: return None
        l, r = 0, len(numbers)-1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1, r+1]
            if sum < target: l+=1
            if sum > target: r-=1
        return None
# @lc code=end

