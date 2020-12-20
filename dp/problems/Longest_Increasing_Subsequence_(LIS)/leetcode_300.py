# -*- coding:utf-8 -*-
""" leetcode-300 最长上升子序列

[题目]：
        给定一个**无序**的整数数组，找到其中最长上升子序列的**长度**。

示例:
	输入: [10,9,2,5,3,7,101,18]
	输出: 4
	解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
"""

class Solution:
    def lengthOfLIS(self, nums):
        if nums == []:
            return 0
        # dp[i] 表示以 nums[i]结尾的子序列中最长递增长度
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                # 递增条件判断
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


arr = [10, 9, 2, 5, 3, 7, 101, 18]
print(Solution().lengthOfLIS(arr))