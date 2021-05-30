#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

from typing import List
from python3.aatool.TreeT import TreeNode, createBTree

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 找出目标节点的前序节点
    def findAncestor(self, root: TreeNode, target: TreeNode, ancestor: List[TreeNode]) -> bool:
        if not root: return False
        if root==target or self.findAncestor(root.left, target, ancestor) or self.findAncestor(root.right, target, ancestor):
            ancestor.append(root)
            return True
        return False
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pAncestor, qAncestor = [], []
        self.findAncestor(root, p, pAncestor)
        self.findAncestor(root, q, qAncestor)
        # 找出最接近的公共节点
        i, j = len(pAncestor)-1, len(qAncestor)-1
        while i>-1 and j>-1:
            if pAncestor[i] == qAncestor[j]:
                i, j = i-1, j-1
            else:
                break
        return pAncestor[i+1]
# @lc code=end

root = createBTree([6,2,8,0,4,7,9], 0)
Solution().lowestCommonAncestor(root, root.left, root.left.right)