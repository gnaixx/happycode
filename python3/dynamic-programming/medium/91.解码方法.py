#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    # 边界处理太恶心
    def numDecodings(self, s: str) -> int:
        cnt = [1,1] + [0] * len(s)
        s = "99" + s #添加虚拟头部，以便不用对头部做特殊处理
        for i in range(2, len(s)):
            if(10 <= int(s[i-1:i+1]) <= 26): #s[i]可与s[i-1]组合
                cnt[i] += cnt[i-2]
            if(s[i] != '0'): #s[i]可单独解码
                cnt[i] += cnt[i-1]
        return cnt[-1]
# @lc code=end

print(Solution().numDecodings('112'))