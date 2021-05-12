#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postOrder(self, root: TreeNode, list: List[int]):
        if not root:
            return
        self.postOrder(root.left, list)
        self.postOrder(root.right, list)
        list.append(root.val)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.postOrder(root, ans)
        return ans
# @lc code=end

