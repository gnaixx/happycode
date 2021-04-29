#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

from python3.aatool.LinkT import ListNode, createSLink

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummyNode = ListNode(val=0, next=head)
        curNode = dummyNode
        while curNode.next:
            if curNode.next.val == val:
                curNode.next = curNode.next.next
            else:
                curNode = curNode.next
        return dummyNode.next
# @lc code=end

Solution().removeElements(createSLink([7,7,7,7]), 7)
