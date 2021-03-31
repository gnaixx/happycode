#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'
        string = self.countAndSay(n -1)

        ans, maps, count, pre = '', [], 0, ''
        for c in string:
            if count>0 and list(maps[count-1].keys())[0] == c:
                maps[count-1][c] += 1
            else:
                maps.append({c:1})
                count += 1
        for map in maps:
            key = list(map.keys())[0]
            ans += str(map[key]) + key
        return ans
            
# @lc code=end

Solution().countAndSay(5)