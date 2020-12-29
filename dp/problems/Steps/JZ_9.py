# -*- coding:utf-8 -*-
""" 剑指offer-9 —— 进阶爬楼梯（每次前进最多 n 层）
[题目]：
        一只青蛙一次可以跳上 `1` 级台阶，也可以跳上 `2` 级……它也可以跳上 `n` 级。
        求该青蛙跳上一个 `n` 级的台阶总共有多少种跳法。
"""

# [思路]：dp[i]: 表示i个台阶的跳法数，由题设得到
#
#       dp[i] = dp[i-1] + dp[i-2] + ... + dp[1]
#     dp[i-1] = dp[i-2] + dp[i-3] + ... + dp[1]
# ==> dp[i] = 2*dp[i-1], dp[1]=1
# ==> dp[i] = 2^(i-1)

class Solution:
    def jumpFloorII(self, number):
        # write code here
        dp = [1 for i in range(number)]
        for i in range(1, number):
            dp[i] = 2 * dp[i-1]
        return dp[-1]


if __name__ == '__main__':
    while True:
        try:
            num = int(input())
            print(Solution().jumpFloorII(num))
        except:
            break