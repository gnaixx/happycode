#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def format(self, rows):
        s = ''
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                if rows[i][j]:
                    s += rows[i][j]
        return s

    def convert(self, s: str, numRows: int) -> str:        
        if numRows==1:
            return s
        rows = [[] for i in range(numRows)]
        index = 0
        for j in range(1000):
            for i in range(numRows):
                if j%(numRows-1)==0 or (i+j)%(numRows-1)==0:
                    rows[i].append(s[index])
                    index += 1
                else:
                    rows[i].append(None)
                if index >= len(s):
                    return self.format(rows)

# @lc code=end

Solution().convert('A', 1)
