#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

from python3.aatool.TreeT import TreeNode, createBTree

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def childSum(self, root: TreeNode, targetSum: int, sum: int) -> bool:
        if not root.left and not root.right:
            return sum + root.val == targetSum
        hasLeft, hasRight = False, False
        if root.left:
            hasLeft = self.childSum(root.left, targetSum, sum+root.val)
        if root.right:
            hasRight = self.childSum(root.right, targetSum, sum+root.val)
        return hasLeft or hasRight
        
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        return self.childSum(root, targetSum, 0)
        
# @lc code=end

Solution().hasPathSum(createBTree([5,4,8, 11,None,13,4,7,2,None,None,None,1], 0), 22)