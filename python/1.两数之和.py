#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            num2 = target - num
            if num2 in hashmap:
                return [hashmap[num2], index]
            hashmap[num] = index
        return None

# @lc code=end

