#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        # 必须set否则会超时
        tmpA, tmpB, nodeList = headA, headB, set() 
        while tmpA:
            nodeList.add(tmpA)
            tmpA = tmpA.next
        
        while tmpB:
            if tmpB in nodeList:
                return tmpB
            tmpB = tmpB.next
        return None
# @lc code=end

