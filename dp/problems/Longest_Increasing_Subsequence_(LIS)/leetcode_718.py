# -*- coding:utf-8 -*-

""" leetcode-718. 最长重复子数组（二维）（==要求连续==）
[题目]：
        给两个整数数组 `A` 和 `B` ，返回两个数组中公共的、长度最长的**子数组的长度**。

示例：
	输入：
		A: [1,2,3,2,1]
		B: [3,2,1,4,7]
	输出：3
	解释：长度最长的公共子数组是 [3, 2, 1] 。
"""
from typing import List

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if not (A != [] and B != []):
            return 0

        # dp[i][j] 表示A[0],...,A[i]与B[0],...,B[j]中最长公共子数组长度
        dp = [[0 for _ in range(len(B))] for __ in range(len(A))]
        for i in range(len(A)):
            # 若A中有元素A[i]与B[0]相同，那么说明最长公共子数组长度为1，即dp[i][0]=1
            if A[i] == B[0]:
                dp[i][0] = 1
        for j in range(len(B)):
            # 若B中有元素B[j]与A[0]相同，那么同理
            if B[j] == A[0]:
                dp[0][j] = 1

        for i in range(1, len(A)):
            for j in range(1, len(B)):
                # 1，若两个数组当前遍历的最后一个元素相同，那么只需要判断之前的子数组
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                # 2，若不相同，说明以最后一个元素结尾的子数组长度为0
                else:
                    dp[i][j] = 0
        # 记录最大公共子数组长度
        ans = 0
        for i in range(len(dp)):
            ans = max(ans, max(dp[i]))
        return ans

if __name__=='__main__':
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    print(Solution().findLength(A, B))