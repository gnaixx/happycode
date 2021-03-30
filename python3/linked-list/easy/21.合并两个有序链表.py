#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

import sys
sys.path.append('/Users/xiangqing.xxq/Workspace/Code/tooy/keepcode/python3')
from aatool.LinkT import ListNode
from aatool.LinkT import createLink, toList

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     if l1==None and l2==None: return None
    #     if l1==None: return l2
    #     if l2==None: return l1

    #     if l1.val > l2.val:
    #         node = l2
    #         l2 = l2.next
    #     else:
    #         node = l1
    #         l1 = l1.next
    #     answer = node

    #     while l1!=None or l2!=None:
    #         if l1==None and l2!=None:
    #             node.next = l2
    #             l2 = l2.next
    #         if l2==None and l1!=None:
    #             node.next = l1
    #             l1 = l1.next
            
    #         if l1==None or l2==None:
    #             node = node.next
    #             continue
            
    #         if l1.val > l2.val:
    #             node.next = l2
    #             l2 = l2.next
    #         else:
    #             node.next = l1
    #             l1 = l1.next
    #         node = node.next
    #     return answer
# @lc code=end

print(toList(Solution().mergeTwoLists(createLink([-9,3]), createLink([5,7]))))
