from typing import List
import queue

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLink(array: List[int]) -> ListNode:
    preNode = None
    for i in range(len(array)-1, -1, -1):
        preNode = ListNode(array[i], preNode)
    return preNode


def toList(node: ListNode) -> List[int]:
    array = []
    while(node != None):
        array.append(node.val)
        node = node.next
    return array