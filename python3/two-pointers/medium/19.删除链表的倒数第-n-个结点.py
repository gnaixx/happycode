#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

from python3.aatool.LinkT import ListNode, createSLink

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     curMap, preMap, preNode, tmp = [], [], None, head
    #     while tmp:
    #         curMap.append(tmp)
    #         preMap.append(preNode)
    #         preNode = tmp
    #         tmp = tmp.next
    #     dIndex = len(curMap) - n
    #     curNode = curMap[dIndex]
    #     preNode = preMap[dIndex]
    #     if preNode:
    #         preNode.next = curNode.next
    #     else:
    #         head = head.next
    #     return head
    def removeNthFromEnd(self, head, n):
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next
# @lc code=end

Solution().removeNthFromEnd(createSLink([1,2,3,4,5]), 2)
