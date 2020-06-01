#
# @lc app=leetcode.cn id=1025 lang=python3
#
# [1025] 除数博弈
#

# @lc code=start
class Solution:
    # 1.最终结果应该是占到 2 的赢，占到 1 的输；
    # 2.若当前为奇数，奇数的约数只能是奇数或者 1，因此下一个一定是偶数；
    # 3.若当前为偶数，偶数的约数可以是奇数,可以是偶数,也可以是 1，因此直接减 1，则下一个是奇数；
    # 4.因此，奇则输，偶则赢
    # return N % 2 ==0;
    def divisorGame(self, N: int) -> bool:
        must = [False] * (N+2)
        must[1], must[2] = False, True
        for i in range(3, N+1):
            for j in range(1, int(N/2)):
                if i%j==0 and not must[i-j]:
                    must[i] = True
                    break
        return must[N]    
# @lc code=end

Solution().divisorGame(3)

