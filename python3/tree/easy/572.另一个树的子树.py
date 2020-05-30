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
        if s == None and t == None: 
            return True
        if s == None or t == None: 
            return False
        if s.val != t.val: 
            return False
        return self.isSameTree(s.left, t.left) or self.isSameTree(s.right, t.right)


    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if t == None: 
            return True
        if s == None: 
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) or self.isSameTree(s, t)
        
# @lc code=end

