# -*- coding:utf-8 -*-
""" 商汤笔试(2018.9.7笔试) 再进阶爬楼梯（n 层楼梯，最多爬 m 层）
[题目]：
        一层楼共有 `n` 级台阶，一次可以上至少 `1` 级但不超过 `m` 级台阶，求有多少种不同的上楼方案数。
        由于结果可能很大，你只需要输出结果对 `10007` 取模的值即可.
"""

# [思路]：未优化
# 记 dp[n] 表示台阶总数为n，每次最多前进m层时，不同的上楼方法总数。
# 记 step 为第一步选择上升的层数
# 		  step=1   step=2           step=m
# dp[n] = dp[n-1] + dp[n-2] + ... + dp[n-m]    (n >= m)

class Solution:
    def Steps_nm(self, n, m):
        if n == 1:
            return 1
        elif n == 2:
            if m == 1:
                return 1
            else:
                return 2
        else:
            dp = [1] + [i for i in range(1, n+1)]
            for i in range(3, n+1):
                # 下面完成dp[i] = dp[i-1] + ... + dp[i-m]
                for j in range(i-1, i-m-1, -1):
                    if j >= 0:
                        dp[i] += dp[j]
            return dp[n]