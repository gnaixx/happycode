#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        headNode = None
        dummyNode = ListNode(0, headNode)
        while any(lists):
            minIndex, minValue = 0, float('inf')
            for i, v in enumerate(lists):
                if not v: continue
                if v.val <= minValue:
                    minValue, minIndex = v.val, i
            if headNode:
                headNode.next = lists[minIndex]
                headNode = headNode.next
            else:
                headNode = lists[minIndex]
                dummyNode.next = headNode
            if lists[minIndex]:
                lists[minIndex] = lists[minIndex].next
        return dummyNode.next
# @lc code=end

# Solution().mergeKLists([createSLink([1,4,5]), createSLink([1,3,4]), createSLink([2,6])])
Solution().mergeKLists([])
