#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

from python3.aatool.LinkT import ListNode, createSLink

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 去除k=0,空链表，单链表
        if not k or not head or not head.next: return head
        # 计算链表长度
        cur, p1, p2, s = head, head, head, 1
        while cur.next: s, cur = s+1, cur.next
        # 计算移动长度
        if not (k:=k%s): return head
        # 快指针先走k步,如果走到最后一个节点直接返回
        while k: k, p1 = k-1, p1.next
        if not p1: return head
        # 快慢指针同时移动，快指针走到链尾，慢指针的下个节点为新链表头
        while p1.next:
            if not p2: p2 = head
            p2, p1 = p2.next, p1.next
        p1.next, head, p2.next = head, p2.next, None
        return head
# @lc code=end

Solution().rotateRight(createSLink([1,2]), 2)
