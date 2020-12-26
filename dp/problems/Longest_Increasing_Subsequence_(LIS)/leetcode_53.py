# -*- coding:utf-8 -*-
""" leetcode-53 最大子序列和（可能存在负数）

[题目]：
        给定一个整数数组 `nums` ，
        找到一个具有**最大和的连续子数组**（子数组最少包含一个元素），返回其最大和。

示例:
	输入: [-2,1,-3,4,-1,2,1,-5,4]
	输出: 6
	解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        n = len(nums)
        # dp[i]表示以nums[i]结尾的最大子序列和
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            # 由于存在负数，所以需要对比dp[i-1]和0的大小
            dp[i] = max(0, dp[i-1]) + nums[i]
        return max(dp)