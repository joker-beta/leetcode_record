# -*- codingutf:8 -*-
""" leetcode-1035. 不相交的线 (same as leetcode-1143)
[题目]：
        我们在两条独立的水平线上按给定的顺序写下 `A` 和 `B` 中的整数。
        现在，我们可以绘制一些连接两个数字 `A[i]` 和 `B[j]` 的直线，只要 `A[i] == B[j]`，
        且我们绘制的直线不与任何其他连线（非水平线）相交。
        以这种方法绘制线条，并返回我们**可以绘制的最大连线数**。
"""

# [思路]：等价于找到A和B中相同的整数个数的最大值
#		 也就是找出A和B中相同子序列的的最大个数。

from typing import List
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        if not (A != [] and B != []):
            return 0
        # dp[i][j] 表示以A[i]和B[j]结尾的子序列最长的公共子串长度
        dp = [[1 for j in range(len(B))] for i in range(len(A))]

        # 处理二维列表边界
        for i in range(len(A)):
            if A[i] != B[0]:
                dp[i][0] = 0
            else:
                break
        for j in range(len(B)):
            if B[j] != A[0]:
                dp[0][j] = 0
            else:
                break
        # 处理二维列表内部
        for i in range(1, len(A)):
            for j in range(1, len(B)):
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]


