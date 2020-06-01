#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

from typing import List

# @lc code=start
class Node:
    def __init__(self, degree=0, start=0, end=0):
        self.degree = degree
        self.start = start
        self.end = end

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        nodeMap = {}
        maxDegree, minLen = 0, 50000
        for i in range(len(nums)):
            if nums[i] not in nodeMap:
                node = Node(0, 0, 0)
                nodeMap[nums[i]] = node
            node = nodeMap[nums[i]]
            if node.degree == 0:
                node.start = i
            node.end = i
            node.degree += 1
            maxDegree = node.degree if maxDegree < node.degree else maxDegree

        for k, v in nodeMap.items():
            if v.degree < maxDegree:
                continue
            minLen = min(minLen, v.end - v.start + 1)
        return minLen
        
# @lc code=end

Solution().findShortestSubArray([1, 2, 2, 3, 1])

