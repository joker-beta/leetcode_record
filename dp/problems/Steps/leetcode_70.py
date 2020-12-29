# -*- coding:utf-8 -*-
""" leetcode-70. 爬楼梯（每次前进 1 或 2 层台阶）
[题目]：
        假设你正在爬楼梯。需要 `n` 阶你才能到达楼顶。每次你可以爬 `1` 或 `2` 个台阶。
        你有多少种不同的方法可以爬到楼顶呢？注意：给定 `n` 是一个正整数

示例 1：
	输入： 2
	输出： 2
	解释： 有两种方法可以爬到楼顶。
			1.  1 阶 + 1 阶
			2.  2 阶
示例 2：
	输入： 3
	输出： 3
	解释： 有三种方法可以爬到楼顶。
		1.  1 阶 + 1 阶 + 1 阶
		2.  1 阶 + 2 阶
		3.  2 阶 + 1 阶
"""

class Solution_1:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 1
        # dp[i]表示i个台阶的上楼梯方法数
        dp = [1 for _ in range(n+1)]
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]


class Solution_2:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 1
        pre, lat = 1, 1
        for i in range(2, n+1):
            tmp = lat
            lat += pre
            pre = tmp
        return lat


if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            print(Solution_1().climbStairs(n))
            print(Solution_2().climbStairs(n))
        except:
            break
