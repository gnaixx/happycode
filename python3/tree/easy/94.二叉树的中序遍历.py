#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

from typing import List


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root: TreeNode, list: List[int]):
        if not root:
            return
        self.inOrder(root.left, list)
        list.append(root.val)
        self.inOrder(root.right, list)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.inOrder(root, ans)
        return ans
# @lc code=end

