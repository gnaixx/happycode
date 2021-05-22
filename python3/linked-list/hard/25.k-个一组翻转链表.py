#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
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
    # 反转链表的k个节点并返回反转后最后一个节点
    def reverse(self, preNode: ListNode, head: ListNode, k: int) -> ListNode:
        temp, stack = head, []
        for i in range(k):
            if temp:
                stack.append(temp)
                temp = temp.next
            else:
                break
        if len(stack) < k:
            return None
        for i in range(k-1, -1, -1):
            preNode.next = stack[i]
            preNode = preNode.next
            if i == k-1:
                lstNode = stack[i].next
            if i == 0:
                stack[i].next = lstNode
        return preNode

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummyNode = ListNode(val=0, next=head)
        preNode = dummyNode
        while preNode:
            preNode = self.reverse(preNode, head, k)
            head = preNode.next if preNode else None
        return dummyNode.next
# @lc code=end

Solution().reverseKGroup(createSLink([1,2,3,4,5]), 1)