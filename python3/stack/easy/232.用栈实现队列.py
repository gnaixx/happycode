#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackIn = []
        self.stackOut = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stackIn.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stackOut:
            return self.stackOut.pop()
        else:
            while len(self.stackIn):
                self.stackOut.append(self.stackIn.pop())
            return self.stackOut.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stackOut:
            return self.stackOut[-1]
        else:
            while len(self.stackIn):
                self.stackOut.append(self.stackIn.pop())
            return self.stackOut[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not len(self.stackIn) and not len(self.stackOut)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

