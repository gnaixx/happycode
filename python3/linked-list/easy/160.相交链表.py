#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#
from python3.aatool.LinkT import ListNode, createSLink

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     if not headA or not headB: return None
    #     # 必须set否则会超时
    #     tmpA, tmpB, nodeList = headA, headB, set() 
    #     while tmpA:
    #         nodeList.add(tmpA)
    #         tmpA = tmpA.next
        
    #     while tmpB:
    #         if tmpB in nodeList:
    #             return tmpB
    #         tmpB = tmpB.next
    #     return None
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        # 非相交最后会一起走到 None
        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa 
# @lc code=end

Solution().getIntersectionNode(createSLink([1, 2, 3]), createSLink([4, 5]))