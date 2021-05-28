#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

from python3.aatool.LinkT import ListNode, createSLink

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # head2 需要作为全局变量处理
    def recursion(self, head1: ListNode):
        if head1:
            if not self.recursion(head1.next):
                return False
            if head1.val != self.head2.val:
                return False
            self.head2 = self.head2.next
        return True
    
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        headNode, tailNode, curNode = head, head, head.next
        while curNode:
            tailNode.next, curNode.next = curNode.next, headNode
            headNode, curNode = curNode, tailNode.next
        return headNode

    def isPalindrome(self, head: ListNode) -> bool:
        # self.head2 = head
        # return self.recursion(head)

        if not head or not head.next: return True
        # 找出中间节点，奇数点归前半段
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 反转后续节点
        rehead = self.reverseList(slow.next)
        # 判断回文
        flag, head2 = True, rehead
        while head2 and flag:
            if head.val != head2.val: flag = False
            head, head2 = head.next, head2.next
        # 反转回去
        slow.next = self.reverseList(rehead)
        return flag
# @lc code=end

Solution().isPalindrome(createSLink([1,2,3,2,1]))
