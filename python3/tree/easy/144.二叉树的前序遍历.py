#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

from python3.aatool.TreeT import TreeNode, createBTree
from typing import List

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrder(self, root: TreeNode, array: List[int]):
        if not root: return
        array.append(root.val)
        self.proOrder(root.left, array)
        self.proOrder(root.right, array)

    def preOrder1(self, root: TreeNode, array: List[int]):
        if not root: return
        stack = [root]
        while stack:
            node = stack.pop()
            array.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        array = []
        self.preOrder1(root, array)
        return array
# @lc code=end

Solution().preorderTraversal(createBTree([1,2,3], 0))