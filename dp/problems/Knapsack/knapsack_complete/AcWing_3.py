# -*- coding:utf-8 -*-
""" AcWing-3 完全背包问题
[题目]:
        有 N 件物品和一个容量是 V 的背包。每种物品都有无限件可用。
        第 i 件物品的体积是 vi，价值是 wi。

        求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
        输出最大价值。

[输入格式]: 第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。
            接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。
[输出格式]: 输出一个整数，表示最大价值。

[数据范围]:
        0 < N, V ≤ 1000
        0 < vi, wi ≤ 1000

[输入样例]:
            4 5
            1 2
            2 4
            3 4
            4 5
[输出样例]：
            8
"""


# dp[i][j] = max(dp[i-1][j], dp[i-1][j-ci]+vi, dp[i-1][j-2*ci]+2*vi,...,dp[i-1][j-k*ci]+k*vi,...)
# dp[i][j-ci] = max(dp[i-1][j-ci], dp[i-1][j-2*ci]+vi, dp[i-1][j-3*ci]+2*vi,...,dp[i-1][j-(k+1)*ci]+k*vi,...)
# ==> dp[i][j] = max(dp[i - 1][j], dp[i][j - ci] + vi)

class Solution_1:
    """二维数组"""
    def fun(self, N, V, goods):
        # dp[i][j] 表示取前i个物品，并且当前背包剩余容量为j时，能获取的最大价值
        dp = [[0 for j in range(V + 1)] for i in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, V + 1):
                # 1，若装不下当前物品arr[i-1]
                if j < goods[i - 1][0]:
                    dp[i][j] = dp[i - 1][j]
                # 2，若能装下物品arr[i-1]，但是可能选择装或者不装
                if j >= goods[i - 1][0]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - goods[i - 1][0]] + goods[i - 1][1])
        return dp[N][V]


class Solution_2:
    """(优化)一维数组"""
    def fun(self, N, V, goods):
        # dp[i] 表示遍历到当前物品时，背包剩余容量为i时，能获取的最大价值
        dp = [0 for _ in range(V + 1)]
        for i in range(1, N + 1):
            for j in range(goods[i - 1][0], V + 1):  # 注意这里是顺序遍历，和01背包不同。
                dp[j] = max(dp[j], dp[j - goods[i - 1][0]] + goods[i - 1][1])
        return dp[-1]


if __name__ == '__main__':
    while True:
        try:
            arr = list(map(int, input().split()))
            N, V = arr[0], arr[1]
            goods = []
            for _ in range(N):
                goods.append(list(map(int, input().split())))
            # print(Solution_1().fun(N, V, goods))
            print(Solution_2().fun(N, V, goods))
        except:
            break