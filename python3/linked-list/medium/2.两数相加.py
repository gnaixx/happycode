#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

from typing import List
from python3.aatool.LinkT import ListNode, createSLink

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root, pre, x = None, None, 0
        while l1 or l2 or x!=0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            x, y = divmod(v1+v2+x, 10)
            node = ListNode(y, None)
            if pre:
                pre.next = node
            else:
                root = node
            pre = node
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return root
# @lc code=end

Solution().addTwoNumbers(createSLink([9,9,9,9,9,9,9]), createSLink([9,9,9,9]))