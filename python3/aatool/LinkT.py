from typing import List
import queue

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __init__(self, val=0, pre=None, next=None):
        self.val = val
        self.pre = pre
        self.next = next


# 创建单向链表
def createSLink(array: List[int]) -> ListNode:
    head = None
    for i in range(len(array)-1, -1, -1):
        head = ListNode(array[i], next=head)
    return head

# 创建双向链表
def createDLink(array: List[int]) -> ListNode:
    head, pre, next = None, None, None
    for i in range(len(array)-1, -1, -1):
        head = ListNode(array[i], pre=pre, next=next)
        if next: next.pre = head
        next = head
    return head

# 转list
def toList(node: ListNode) -> List[int]:
    array = []
    while(node != None):
        array.append(node.val)
        node = node.next
    return array