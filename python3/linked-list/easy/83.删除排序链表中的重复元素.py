#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

import sys
sys.path.append('/Users/xiangqing.xxq/Workspace/Code/tooy/keepcode/python3')

from aatool.LinkT import ListNode, createSLink, toList
from typing import List

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre, cur, bit = head, head, [False] * 200
        while cur:
            if bit[cur.val]:
                pre.next = cur.next
            else:
                bit[cur.val] = True
                pre = cur
            cur = cur.next
        return head
# @lc code=end

print(toList(Solution().deleteDuplicates(createSLink([1,1,2,3,3]))))
# createDLink([1,2,3])
