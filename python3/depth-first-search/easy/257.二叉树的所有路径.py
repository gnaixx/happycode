#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursion(self, root: TreeNode, ans:List[str], s:str):
        if root: s = str(root.val) if not s else s +'->'+str(root.val)
        if not root.left and not root.right: ans.append(s)
        if root.left: self.recursion(root.left, ans, s)
        if root.right: self.recursion(root.right, ans, s)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        self.recursion(root, ans, '')
        return ans
# @lc code=end

