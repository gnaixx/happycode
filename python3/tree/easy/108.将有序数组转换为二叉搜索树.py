#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

from typing import List
from python3.aatool.TreeT import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createNode(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None
        mid = (left+right) // 2
        leftNode = self.createNode(nums, left, mid-1)
        rightNode = self.createNode(nums, mid+1, right)
        return TreeNode(nums[mid], leftNode, rightNode)

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.createNode(nums, 0, len(nums)-1)
# @lc code=end

Solution().sortedArrayToBST([-10,-3,0,5,9])
