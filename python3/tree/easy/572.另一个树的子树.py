#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
#

import sys
sys.path.append('/Users/xiangqing.xxq/Documents/Code/tooy/keepcode/python3')
from aatool.TreeT import createBTree
from aatool.TreeT import preOrder1
from aatool.TreeT import levelOrder
from aatool.TreeT import TreeNode

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

treeNode = createBTree([3, 4, 5, 1, 2], 0)
arrays = []
# preOrder1(treeNode, arrays)
levelOrder(treeNode, arrays)
print(arrays)


