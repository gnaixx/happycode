#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

from typing import List
from python3.aatool.TreeT import preOrder, TreeNode, createBTree, postOrder3, inOrder, postOrder1, postOrder2

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t: 
            return True
        if not s or not t:
            return False
        return s.val==t.val and self.check(s.left, t.right) and self.check(s.right, t.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.check(root.left, root.right)
# @lc code=end

root = createBTree([1,2,3,4,5,6,7], 0)
list = []
preOrder(root, list)
print(list)

list = []
inOrder(root, list)
print(list)

list = []
postOrder1(root, list)
print(list)

list = []
postOrder2(root, list)
print(list)

list = []
postOrder3(root, list)
print(list)