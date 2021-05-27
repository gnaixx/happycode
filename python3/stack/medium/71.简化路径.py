#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split('/')
        for p in paths:
            if not p or p=='.': continue
            if p=='..': 
                if stack: stack.pop()
                continue
            stack.append(p)
        return '/' + '/'.join(stack)
# @lc code=end

Solution().simplifyPath('/a/./b/../../c/')

