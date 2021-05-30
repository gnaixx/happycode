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
    if index < len(array) and array[index]!=None:
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
    stack = [root]
    while stack:
        node = stack.pop()
        arrays.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# 中序遍历(非递归)
def inOrder1(root: TreeNode, arrays: List) -> None:
    stack, node = [], root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        arrays.append(node.val)
        node = node.right

# 后续遍历(非递归)
def postOrder1(root: TreeNode, arrays: List) -> None:
    stack = [root]
    while stack:
        node = stack.pop()
        arrays.append(node.val)
        # 采用和先序遍历一样策略，最后反转
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    arrays = arrays.reverse()

# 后续遍历(非递归)
def postOrder2(root: TreeNode, arrays: List) -> None:
    # temp 保存是第一次访问该节点
    stack, node, temp = [], root, []
    while node or stack:
        while node:
            temp.append(node)
            stack.append(node)
            node = node.left
        node = stack.pop()
        # 如果是第一次访问该节点直接遍历右节点
        if node in temp:
            temp.remove(node)
            stack.append(node)
            node = node.right
        else:
            arrays.append(node.val)
            node = None     

# 后续遍历(非递归)
def postOrder3(root: TreeNode, arrays: List) -> None:
    stack, node, pre = [], root, None
    while node:
        # 单前节点没有子节点或者子节点被访问过则可以添加
        if (not node.left and not node.right) or (pre and (pre==node.left or pre==node.right)):
            arrays.append(node.val)
        else:
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
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

