# -*- coding:utf-8 -*-
""" leetcode-1143. 最长公共子序列（二维）（==不一定连续==）
>[题目]：
        给定两个字符串 `text1` 和 `text2`，返回这两个**字符串**的最长公共**子序列的长度**。
        一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

        例如，`"ace"` 是 `"abcde"` 的子序列，但 `"aec"` 不是 `"abcde"` 的子序列。
        两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
        若这两个字符串没有公共子序列，则返回 `0`。

示例 1:
	输入：text1 = "abcde", text2 = "ace"
	输出：3
	解释：最长公共子序列是 "ace"，它的长度为 3。

示例 2:
	输入：text1 = "abc", text2 = "def"
	输出：0
	解释：两个字符串没有公共子序列，返回 0。
"""

from typing import List
class Solution_1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """计算最大的长度"""
        # 判断字符串为空的情况
        if not (text1 and text2):
            return 0
        # 创建二维数组，dp[i][j]表示字符串text1[0,...,i]和text2[0,...,j]的最长相同子序列长度
        dp = [[1 for j in range(len(text2))] for i in range(len(text1))]
        # 第一行边界
        for j in range(len(text2)):
            if text1[0] != text2[j]:
                dp[0][j] = 0
            # 若出现第一个相同的字符，直接跳过
            else:
                break
        # 第二行边界
        for i in range(len(text1)):
            if text2[0] != text1[i]:
                dp[i][0] = 0
            else:
                break
        # 数组内部
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                # 1，若当前遍历最后位置的字符不相同，则分别对比前一个位置的情况
                if text1[i] != text2[j]:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                # 2，若相同，则同时对比前一个位置的情况
                else:
                    dp[i][j] = dp[i-1][j-1] + 1
        return dp[-1][-1]



class Solution_2:
    def longestSubsequence(self, text1: str, text2: str) -> str:
        """将最大的公共序列输出"""
        n, m = len(text1), len(text2)
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # 输出最长字符串
        if dp[-1][-1] == 0:
            return -1
        ans = []
        i, j = n, m
        while (i > 0) and (j > 0):
            if text1[i-1] == text2[j-1]:
                ans.append(text1[i-1])
                i -= 1
                j -= 1
                continue
            else:
                if dp[i][j-1] >= dp[i-1][j]:
                    j -= 1
                else:
                    i -= 1
        return ''.join(reversed(ans))



if __name__=='__main__':
    text1 = "abcde"
    text2 = "ace"
    print(Solution_1().longestCommonSubsequence(text1, text2))
    print(Solution_2().longestSubsequence(text1, text2))