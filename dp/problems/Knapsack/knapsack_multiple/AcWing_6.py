# -*- coding:utf-8 -*-
""" AcWing-6 多重背包问题_III
[题目]:
        有 N 件物品和一个容量是 V 的背包。
        第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。

        求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
        输出最大价值。

[输入格式]: 第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。
            接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。
[输出格式]: 输出一个整数，表示最大价值。

[数据范围]:
         0 < N ≤ 1000
         0 < V ≤ 20000
         0 < vi, wi, si ≤ 20000

[输入样例]:
            4 5
            1 2 3
            2 4 1
            3 4 3
            4 5 2
[输出样例]：
            10

[参考]：
(python版本)：https://www.acwing.com/solution/content/15198/
https://www.acwing.com/solution/content/15671/
https://www.acwing.com/solution/content/1537/
"""

# [思路]：我们根据一般多重背包问题的分析知道状态转移方程为
#           F[i, j] = max{F[i - 1, j - k*vi] + k*wi: 0 <= k <= si}
# 在AcWing-4中，由于数据范围较小我们直接通过循环嵌套进行处理。
# 在AcWing-5中，数据范围变大一些，我们通过对si进行二进制分组的策略，将总的时间复杂度降低了。
# 在当前的问题中，数据范围变得更大，我们考虑将问题转化为单调队列优化问题(或者说滑动窗口策略)。
#
# 注意到上面的方程
#       F[i, j] = max{F[i - 1, j - k*vi] + k*wi: 0 <= k <= si, 0 < j - k*ci}
# 化简为一维形式
#       f[j] = max{f[j - k*ci] + k*wi: 0 <= k <= si, 0 < j - k*ci}
# 发现f[j]仅仅依赖f[j - k*ci]，按照依赖性对f[j]进行 模ci 分组。
# 数学推导：
#       f[j + p*ci] = max{f[j + k*ci] + (p-k)*wi: 0 <= k <= p}
# ==>   f[j + p*ci] - p*wi = max{f[j + k*ci] - k*wi: 0 <= k <= p}
# 那么我们将 f[j + p*ci] - p*wi 转换成了标准的滑动窗口单调队列形式，即
#                   f[x] - (x - j)/ci * wi，
# 对于 x = j + p*ci 构成单调队列。



from collections import deque

class Solution_1:
    def fun(self, N, V, goods):
        # 设置单调队列
        q = deque()
        dp = [0 for _ in range(V + 1)]
        # 对N种物品进行迭代
        for i in range(N):
            [vi, wi, si] = goods[i]
            # 对当前物品goods[i]的各重量迭代
            for j in range(vi):
                # 每次新的循环都需要初始化队列
                # 由于这里用单调队列对每种物品的重量进行滑动窗口操作
                q.clear()
                nums = (V - j) // vi  # 剩余的空间最多还能放几个当前物品
                for k in range(nums + 1):
                    val = dp[j + k*vi] - k*wi
                    # 1，若当前队列非空，并且队尾元素记录的元素小于等于当前元素val
                    #    那么为了使得队列存放的数呈现递减趋势，需要将队尾元素删除
                    while q and q[-1][1] <= val:
                        q.pop()
                    # 2，否则，继续往队列中添加元素
                    q.append([k, val])

                    # 存放的个数不能超出物品数量，否则将元素弹出
                    if q[0][0] < k - si:
                        q.popleft()
                    dp[j + k*vi] = q[0][1] + k*wi
        return dp[V]


if __name__ == '__main__':
    while True:
        try:
            N, V = list(map(int, input().split()))
            goods = []  # (vi, wi, si)
            for _ in range(N):
                goods.append(list(map(int, input().split())))
            print(Solution_1().fun(N, V, goods))
        except:
            break
