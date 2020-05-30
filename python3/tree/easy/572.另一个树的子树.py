#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t: 
            return True
        if not s or not t:
            return False
        return s.val==t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)


    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t: 
            return True
        if not s or not t:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) or self.isSameTree(s, t)
        
# @lc code=end

