# -*- coding:utf-8 -*-
""" leetcode-416 分割等和子集（01背包容量：半数组累加和）
[题目]：
        给定一个只包含正整数的非空数组。
        是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

[注意]:
    * 每个数组中的元素不会超过`100`
    * 数组的大小不会超过`200`

示例 1:
	输入: [1, 5, 11, 5]
	输出: true
	解释: 数组可以分割成 [1, 5, 5] 和 [11].

示例 2:
	输入: [1, 2, 3, 5]
	输出: false
	解释: 数组不能分割成两个元素和相等的子集.
"""
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if nums == []:
            return False
        # 先统计累加和
        target = sum(nums)
        # 1，若数组累加和为奇数，则不能平分为两个等值子数组
        if target%2 != 0:
            return False
        # 2，否则，取累加和平分后的半值
        target = target//2

        # 接下来将问题转化为，背包容量为target(半值)，选择连续的数组装入的01背包问题
        n = len(nums)
        # dp[i][j]表示当前背包容量为j，并考虑前i个元素时，背包是否能装满
        dp = [[False for j in range(target + 1)] for i in range(n)]

        # 处理边界
        # dp[0][1],dp[0][2],...,dp[0][sum//2]表示背包容量为*，但什么都不装，显然不能装满
        # dp[1][0],dp[2][0],...,dp[n][0]表示背包容量为0那么若什么都不装，显然背包能装满
        dp[0][0] = True

        # 对于dp[i][j]的分析
        for i in range(1, n):
            for j in range(target+1):
                # 1，若第i个物品nums[i-1]不装入背包，也就是装不下nums[i-1]时，前i-1个的情况和前i个情况相同
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                # 2，若第i个物品nums[i-1]可以装入背包，
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]

        return dp[-1][-1]



