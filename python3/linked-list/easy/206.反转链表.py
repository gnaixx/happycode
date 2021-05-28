#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
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
    # 递归
    def recursion(self, preNode:ListNode, head: ListNode) -> ListNode:
        if head and head.next: 
            # 返回尾部
            tailNode = self.recursion(head, head.next)
            # head.next 保存新的头节点
            preNode.next = head.next
            # 单前节点移到尾部
            tailNode.next, head.next = head, tailNode.next
            return tailNode.next
        else:
            return head

    # 迭代
    def iteration(self, head:ListNode) -> ListNode:
        # 空链，单节点链直接返回
        if not head or not head.next: return head
        # 从第二个节点开始遍历
        headNode, tailNode, curNode = head, head, head.next
        while curNode:
            # 当前节点后一个节点移到最新尾部，最新表头移到当前节点后
            tailNode.next, curNode.next = curNode.next, headNode
            # 更新最新节点&单前节点
            headNode, curNode = curNode, tailNode.next
        return headNode

    def reverseList(self, head: ListNode) -> ListNode:
        return self.iteration(head)
        # dummyNode = ListNode(val=0, next=head)
        # self.recursion(dummyNode, head)
        # return dummyNode.next
# @lc code=end

Solution().reverseList(createSLink([1,2,3,4,5]))