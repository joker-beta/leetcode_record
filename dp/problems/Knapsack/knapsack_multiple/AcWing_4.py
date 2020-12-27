# -*- coding:utf-8 -*-
""" AcWing-4 多重背包问题_I
[题目]:
        有 N 件物品和一个容量是 V 的背包。
        第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。

        求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
        输出最大价值。

[输入格式]: 第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。
            接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。
[输出格式]: 输出一个整数，表示最大价值。

[数据范围]:
         0 < N, V ≤ 100
         0 < vi, wi, si ≤ 100

[输入样例]:
            4 5
            1 2 3
            2 4 1
            3 4 3
            4 5 2
[输出样例]：
            10
"""

# [思路]：我们模拟装包过程得到下面的状态转移方程
# dp[i][j] = max({dp[i-1][j-k*vi]+k*wi: 0 <= k <= si})
# 根据方程迭代的过程，我们可以计算出时间复杂度为 O(N*V*sum_{i}si)
# 由于这题给出的数据范围比较小，对于上面的复杂度是可以接受的，所以下面代码实现就直接通过循环嵌套。


class Solution_1:
    """二维数组"""
    def fun(self, N, V, goods):
        dp = [[0 for j in range(V + 1)] for i in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(V, -1, -1):  # 注意这里是逆序遍历！！！
                for k in range(goods[i - 1][2] + 1):
                    if j >= k * goods[i - 1][0]:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j - k * goods[i - 1][0]] + k * goods[i - 1][1])
        return dp[-1][-1]


class Solution_2:
    """(优化)一维数组"""
    def fun(self, N, V, goods):
        dp = [0 for _ in range(V + 1)]
        for i in range(1, N + 1):
            for j in range(V, -1, -1):  # 注意这里是逆序遍历！！！
                for k in range(goods[i - 1][2] + 1):
                    if j >= k * goods[i - 1][0]:
                        dp[j] = max(dp[j], dp[j - k * goods[i - 1][0]] + k * goods[i - 1][1])
        return dp[-1]


if __name__ == '__main__':
    while True:
        try:
            N, V = list(map(int, input().split()))
            goods = []  # 存放(vi, wi, si)
            for _ in range(N):
                goods.append(list(map(int, input().split())))
            # print(Solution_1().fun(N, V, goods))
            print(Solution_2().fun(N, V, goods))
        except:
            break
