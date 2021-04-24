#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyNode = ListNode(0, head)
        preNode = dummyNode
        while head:
            nextNode = head.next
            if not nextNode:
                break
            preNode.next, head.next, nextNode.next = nextNode, nextNode.next, head
            preNode = head
            head = head.next
        return dummyNode.next 
# @lc code=end

