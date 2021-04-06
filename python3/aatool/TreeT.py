from typing import List
import queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 创建二叉树
def createBTree(array: List, index: int) -> TreeNode:
    treeNode = None
    if index < len(array):
        treeNode = TreeNode(array[index], createBTree(array, 2*index+1), createBTree(array, 2*index+2))
    return treeNode

# 前序遍历
def preOrder(root: TreeNode, array: List) -> None:
    if not root: 
        return
    array.append(root.val)
    preOrder(root.left, array)
    preOrder(root.right, array)

# 中序遍历
def inOrder(root: TreeNode, array: List) -> None:
    if not root: 
        return
    inOrder(root.left, array)
    array.append(root.val)
    inOrder(root.right, array)

# 后续遍历
def postOrder(root: TreeNode, arrays: List) -> None:
    if not root:
        return
    postOrder(root.left, arrays)
    postOrder(root.right, arrays)
    arrays.append(root.val)
    
# 前序遍历(非递归)
def preOrder1(root: TreeNode, arrays: List) -> None:
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        arrays.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# 中序遍历(非递归)
def inOrder1(root: TreeNode, arrays: List) -> None:
    stack = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        arrays.append(node.val)
        node = node.right

# 后续遍历(非递归)
def postOrder1(root: TreeNode, arrays: List) -> None:
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        arrays.append(node.val)
        # 采用和先序遍历一样策略，最后反转
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    arrays = arrays.reverse()

# 层序遍历
def levelOrder(root: TreeNode, arrays: List) -> None:
    queues = queue.Queue()
    queues.put(root)
    while not queues.empty():
        node = queues.get()
        arrays.append(node.val)
        if node.left:
            queues.put(node.left)
        if node.right:
            queues.put(node.right)

