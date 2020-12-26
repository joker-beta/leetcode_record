# -*- coding:utf-8 -*-
""" leetcode-673 最长递增子序列的个数（LIS）
[题目]：给定一个**未排序**的整数数组，找到最长递增子序列的个数。

示例 1:
	输入: [1,3,5,4,7]
	输出: 2
	解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。

示例 2:
	输入: [2,2,2,2,2]
	输出: 5
	解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
"""

# [思路]：dp[i]表示以nums[i]结尾的最长递增子序列的长度
# dp 初始化为1，因为nums[i]自身可以形成一个长度为1的最长递增序列。
# 遍历 [0,...,i]，再套一层，其中j<i。
#   1，当nums[j] < nums[i]，说明以[...,j,i]这段可以形成最长递增序列，长度为 dp[j]+1，
#      其中dp[j]是以nums[j]结尾的最长递增序列的长度。
#   2，当nums[j] >= nums[i]，以[...,j,i]是不能形成最长递增序列的，为dp[i]其被初始化为1了。
# 接下来，要统计最长递增序列的个数，准备长度为n的数组counter，定义count[i]为以nums[i]结尾的最长递增子序列的组合数，
# 这其中有两个限定条件，一个是以nums[i]结尾，另外一个是最长递增序列。
#
# 1，当dp[j]+1>dp[i]，说明第一次找到以nums[i]结尾的最长递增子序列，长度为dp[j]+1，
#    进而可以推出counter[i] = counter[j]以nums[i]结尾的最长递增子序列的组合数等于以nums[j]结尾的最长递增子序列的组合数。
# 2，当dp[j]+1=dp[i],说明这个长度已经找到过一次，那么 counter[i] += counter[j]，
#    即现在的组合方式+counter[j]的组合方式。

from typing import List
class Solution_1:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        # dp[i]表示以nums[i]为最后一个元素的最长递增序列长度
        dp = [1 for _ in range(len(nums))]
        # count[i] 表示以nums[i]结尾的最长递增序列个数
        count = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                # 若存在以nums[i]为最后一个元素的最长递增子序列
                # 那么通过递归来考虑i之前的情况，进一步更新dp[i]
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[i] == dp[j] + 1:
                        count[i] += count[j]
        m = max(dp)
        res = 0
        for i in range(len(dp)):
            if dp[i] == m:
                res += count[i]
        return res



